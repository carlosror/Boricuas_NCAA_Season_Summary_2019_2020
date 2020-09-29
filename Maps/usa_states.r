library(sf)
library(dplyr)
library(readr)
library(ggplot2)

# https://stackoverflow.com/questions/50859765/chloropleth-map-with-geojson-and-ggplot2

usa_shp <- read_sf('gz_2010_us_040_00_20m.json')
usa_data <- read_csv('State_Populations.csv')
usa_shp_mainland <- usa_shp[usa_shp$NAME != "Alaska" & usa_shp$NAME != "Puerto Rico" & usa_shp$NAME != "Hawaii",]

# calculate points at which to plot labels
# centroids <- nepal_shp %>% 
    # st_centroid() %>% 
    # bind_cols(as_data_frame(st_coordinates(.)))    # unpack points to lat/lon columns

# usa_data2 <- filter(nepal_data, `Sub Group` == "HPI")
# nepal_data2 <- mutate(nepal_data2, District = toupper(District))
usa_data_join <- left_join(usa_shp_mainland, usa_data, by = c('NAME' = 'State'))

p <- ggplot(usa_data_join) + geom_sf(aes(fill = Population)) 
print(p)