library(sf)
library(dplyr)
library(readr)
library(ggplot2)
library(grid)
library(gridExtra)
library(cowplot)

# https://stackoverflow.com/questions/50859765/chloropleth-map-with-geojson-and-ggplot2

usa_shp <- read_sf('gz_2010_us_040_00_20m.json')
usa_shp_mainland <- usa_shp[usa_shp$NAME != "Alaska" & usa_shp$NAME != "Puerto Rico" & usa_shp$NAME != "Hawaii",]

# calculate points at which to plot labels
centroids <- usa_shp_mainland %>% 
    st_centroid() %>% 
    bind_cols(as_data_frame(st_coordinates(.)))    # unpack points to lat/lon columns

# Reading the file created by write_csv_files.r
all_players <- read.csv("./../Women/all_players.csv", encoding = "UTF-8")

player_counts_states <- as.data.frame(table(all_players$State), col.names = c("State", "PlayerCount"))
colnames(player_counts_states) <- c("State", "PlayerCount")
player_counts_states$State <- as.character(player_counts_states$State)

usa_data_join <- left_join(usa_shp_mainland, player_counts_states, by = c('NAME' = 'State'))

centroids_join <- left_join(centroids, player_counts_states, by = c('NAME' = 'State'))

# Write player_counts_states to csv
# player_counts_states <- player_counts_states[order(player_counts_states$State),]
# player_counts_states$State[player_counts_states$State == "Washington, D.C."] <- "Washington D.C."
# write.csv(player_counts_states, file = "player_counts_states.csv", row.names = FALSE, quote = FALSE)

theme_map <- function(...) {
  theme_minimal() +
  theme(
    #text = element_text(family = "Ubuntu Regular", color = "#22211d"),
    # axis.line = element_blank(),
    axis.text.x = element_blank(),
    axis.text.y = element_blank(),
    axis.ticks = element_blank(),
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    # panel.grid.minor = element_line(color = "#ebebe5", size = 0.2),
    panel.grid.major = element_line(color = "#ffffff", size = 0.2),
    plot.title = element_text(hjust = 1.6, colour = "dodgerblue4", size = 32),
    plot.subtitle = element_text(hjust = 0.85, colour = "dodgerblue4", size = 20),
    # plot.margin = margin(0, 24, 0, 0, "pt"),
    # panel.grid.minor = element_blank(),
    # plot.background = element_rect(fill = "#f5f5f2", color = NA), 
    # panel.background = element_rect(fill = "#f5f5f2", color = NA), 
    # legend.background = element_rect(fill = "#f5f5f2", color = NA),
    # panel.border = element_blank(),
    ...
  )
}

p <- ggplot(usa_data_join) + geom_sf(color = "white", fill = "light gray") + 
            geom_point(aes(X, Y, size=PlayerCount), data = centroids_join, pch=21, color = "white", fill='cornflowerblue', alpha = 0.5, show.legend = FALSE) +
            scale_size(range = c(5, 30)) +
            geom_text(aes(X, Y, label = NAME), data = centroids, size = 4.0, color = 'dodgerblue4') +
            geom_rect(xmin = -80, xmax = -66.8, ymin = 37, ymax = 47.5, fill = NA, colour = "dodgerblue4", size = 0.5) + 
            theme_map() + ggtitle(label = "Number of players from Puerto Rico by state", subtitle = "Academic year 2019-2020") 
# print(p)

q <- ggplot(usa_data_join) + geom_sf(color = "white", fill = "light gray") + 
            geom_point(aes(X, Y, size=PlayerCount), data = centroids_join, pch=21, color = "white", fill='cornflowerblue', alpha = 0.5, show.legend = FALSE) +
            scale_size(range = c(5, 30)) +
            geom_text(aes(X, Y, label = NAME), data = centroids, size = 3.0, color = 'dodgerblue4') + 
            geom_rect(xmin = -80, xmax = -66.8, ymin = 37, ymax = 47.5, fill = NA, colour = "dodgerblue4", size = 0.5) +
            coord_sf(xlim = c(-80, -66.8), ylim = c(37, 47.5), expand = FALSE) +
            theme_map() + theme(plot.margin = margin(0, 24, 0, 0, "pt"))
# print(q)

# Some options:

# Using gridArrange:
# grid.arrange(p, q, layout_matrix = rbind(c(1, 1, 1, 2), c(1,1,1,NA)))

# https://www.r-spatial.org/r/2018/10/25/ggplot2-sf-3.html
# Using cowplot
print(plot_grid(p, q, nrow = 1, rel_widths = c(2.35, 1)))
# ggsave(filename = "usa_map9.png", , width = 16.05, height = 7.5)