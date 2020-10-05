
library(sf)
library(dplyr)
library(readr)
library(ggplot2)
library(viridis)

# https://stackoverflow.com/questions/50859765/chloropleth-map-with-geojson-and-ggplot2

pr_shp <- read_sf('gz_2010_us_050_00_5m.json')

# Reading the file created by write_csv_files.r
all_players <- read.csv("./../Women/all_players.csv", encoding = "UTF-8")

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

centroids_join <- left_join(centroids, player_counts, by = c('NAME' = 'Hometown'))

# Write player_counts_states to csv
# player_counts <- player_counts[order(player_counts$Hometown),]
# write.csv(player_counts, file = "player_counts_muni.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")

# ***************************************************************************
# The following lines shift the centroid of Mayagüez so it falls on land
# For some reason, you have to run them on the RStudio terminal, then re-plot
# It has to do with encoding
# ***************************************************************************
centroids_join$X[centroids_join$NAME == "Mayagüez"] <- centroids_join$X[centroids_join$NAME == "Mayagüez"] + 0.225
centroids$X[centroids$NAME == "Mayagüez"] <- centroids$X[centroids$NAME == "Mayagüez"] + 0.225
centroids_join$Y[centroids_join$NAME == "Mayagüez"] <- centroids_join$Y[centroids_join$NAME == "Mayagüez"] + 0.025
centroids$Y[centroids$NAME == "Mayagüez"] <- centroids$Y[centroids$NAME == "Mayagüez"] + 0.025

# centroids_join$X[centroids_join$NAME == "Caguas"] <- centroids_join$X[centroids_join$NAME == "Caguas"] + 0.225
# centroids$X[centroids$NAME == "Caguas"] <- centroids$X[centroids$NAME == "Caguas"] + 0.225
# centroids_join$Y[centroids_join$NAME == "Caguas"] <- centroids_join$Y[centroids_join$NAME == "Caguas"] + 0.025
# centroids$Y[centroids$NAME == "Caguas"] <- centroids$Y[centroids$NAME == "Caguas"] + 0.025


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
    plot.title = element_text(hjust = 0.5, colour = "dodgerblue4", size = 32),
    plot.subtitle = element_text(hjust = 0.5, colour = "dodgerblue4", size = 20),
    legend.position = "none",
    # plot.margin = margin(0, 24, 0, 0, "pt"),
    # panel.grid.minor = element_blank(),
    # plot.background = element_rect(fill = "#f5f5f2", color = NA), 
    # panel.background = element_rect(fill = "#f5f5f2", color = NA), 
    # legend.background = element_rect(fill = "#f5f5f2", color = NA),
    # panel.border = element_blank(),
    ...
  )
}

p <- ggplot(pr_data_join) + geom_sf(color = "white", fill = "light gray") + 
            geom_point(aes(X, Y, size=PlayerCount), data = centroids_join, pch=21, color = "white", fill='cornflowerblue', alpha = 0.5) + 
            scale_size(range = c(5, 30)) +
            coord_sf(xlim = c(-67.2, -65.6625)) +
            geom_text(aes(X, Y, label = NAME), data = centroids, size = 4.0, color = 'dodgerblue4') +
            theme_map() +
            ggtitle(label = "Number of players from Puerto Rico by municipality", subtitle = "Academic year 2019-2020")
print(p)
# ggsave(filename = "pr_map3.png", plot = p, width = 16.05, height = 7.5)