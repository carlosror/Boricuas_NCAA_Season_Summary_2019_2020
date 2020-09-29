library(sf)
library(dplyr)
library(readr)
library(ggplot2)
library(viridis)

# https://stackoverflow.com/questions/50859765/chloropleth-map-with-geojson-and-ggplot2

pr_shp <- read_sf('gz_2010_us_050_00_5m.json')

ncaa1 <- read.csv("NCAA_Division_1_players_2019_2020_headers.csv", encoding = "UTF-8")
ncaa2 <- read.csv("NCAA_Division_2_players_2019_2020_headers.csv", encoding="UTF-8")
ncaa3 <- read.csv("NCAA_Division_3_players_2019_2020_headers.csv", encoding="UTF-8")
njcaa1 <- read.csv("NJCAA_Division_1_players_2019_2020_headers.csv", encoding="UTF-8")
njcaa2 <- read.csv("NJCAA_Division_2_players_2019_2020_headers.csv", encoding="UTF-8")
naia <- read.csv("NAIA_players_2019_2020_headers.csv", encoding="UTF-8")

all_players <- rbind(ncaa1, ncaa2, ncaa3, njcaa1, njcaa2, naia)

player_counts <- as.data.frame(table(all_players$Hometown), col.names = c("Pueblo", "PlayerCount"))
colnames(player_counts) <- c("Hometown", "PlayerCount")
player_counts$Hometown <- as.character(player_counts$Hometown)

pr_shp_pr <- pr_shp[pr_shp$STATE == 72,]

# calculate points at which to plot labels
centroids <- pr_shp_pr %>% 
    st_centroid() %>% 
    bind_cols(as_data_frame(st_coordinates(.)))    # unpack points to lat/lon columns

# usa_data2 <- filter(nepal_data, `Sub Group` == "HPI")
# nepal_data2 <- mutate(nepal_data2, District = toupper(District))
pr_data_join <- left_join(pr_shp_pr, player_counts, by = c('NAME' = 'Hometown'))

# https://timogrossenbacher.ch/2016/12/beautiful-thematic-maps-with-ggplot2-only/#a-very-basic-map
# removes the x/y axis, etc
theme_map <- function(...) {
  theme_minimal() +
  theme(
    text = element_text(family = "Ubuntu Regular", color = "#22211d"),
    axis.line = element_blank(),
    axis.text.x = element_blank(),
    axis.text.y = element_blank(),
    axis.ticks = element_blank(),
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    # panel.grid.minor = element_line(color = "#ebebe5", size = 0.2),
    panel.grid.major = element_line(color = "#ebebe5", size = 0.2),
    panel.grid.minor = element_blank(),
    plot.background = element_rect(fill = "#f5f5f2", color = NA), 
    panel.background = element_rect(fill = "#f5f5f2", color = NA), 
    legend.background = element_rect(fill = "#f5f5f2", color = NA),
    panel.border = element_blank(),
    ...
  )
}

p <- ggplot(pr_data_join) + geom_sf(aes(fill = PlayerCount)) + coord_sf(xlim = c(-67.2, -65.6625)) +
                          geom_text(aes(X, Y, label = NAME), data = centroids, size = 2, color = 'red') +
                          theme_map()
# print(p)

# https://timogrossenbacher.ch/2016/12/beautiful-thematic-maps-with-ggplot2-only/#a-very-basic-map
# uses the viridis color scale and fine tunes legend a bit more

q <- p +
  # this is the main part
  theme(legend.position = "bottom") +
  scale_fill_viridis(
    option = "plasma", 
    direction = -1,
    name = "Player Count",
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