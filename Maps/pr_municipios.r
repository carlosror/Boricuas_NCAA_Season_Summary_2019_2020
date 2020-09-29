library(sf)
library(dplyr)
library(readr)
library(ggplot2)
library(viridis)

# https://stackoverflow.com/questions/50859765/chloropleth-map-with-geojson-and-ggplot2

pr_shp <- read_sf('gz_2010_us_050_00_5m.json')
pr_data <- read_csv('prm-est2011-popchg2010-2011.csv')
pr_data$NAME <- substr(pr_data$NAME, 1, nchar(pr_data$NAME) - nchar(" Municipio"))
pr_shp_pr <- pr_shp[pr_shp$STATE == 72,]

# calculate points at which to plot labels
# centroids <- nepal_shp %>% 
    # st_centroid() %>% 
    # bind_cols(as_data_frame(st_coordinates(.)))    # unpack points to lat/lon columns

# usa_data2 <- filter(nepal_data, `Sub Group` == "HPI")
# nepal_data2 <- mutate(nepal_data2, District = toupper(District))
pr_data_join <- left_join(pr_shp_pr, pr_data, by = c('NAME' = 'NAME'))

p <- ggplot(pr_data_join) + geom_sf(aes(fill = POPESTIMATE2010)) + coord_sf(xlim = c(-67.5, -65))
# print(p)

q <- p +
  # this is the main part
  theme(legend.position = "bottom") +
  scale_fill_viridis(
    option = "cividis", 
    direction = -1,
    name = "Population",
    # here we use guide_colourbar because it is still a continuous scale
    guide = guide_colorbar(
      direction = "horizontal",
      barheight = unit(2, units = "mm"),
      barwidth = unit(50, units = "mm"),
      draw.ulim = F,
      title.position = 'top',
      # some shifting around
      title.hjust = 0.5,
      label.hjust = 0.5
  ))
print(q)