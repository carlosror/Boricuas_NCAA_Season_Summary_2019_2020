library(sf)
library(dplyr)
library(readr)
library(ggplot2)
library(geosphere)

usa_shp <- read_sf('gz_2010_us_040_00_20m.json')
usa_shp_mainland_and_pr <- usa_shp[usa_shp$NAME != "Alaska" & usa_shp$NAME != "Hawaii",]

all_players <- read.csv("./../Women/all_players.csv", encoding = "UTF-8")
all_players$Hometown <- as.character(all_players$Hometown)
all_players$Institution <- as.character(all_players$Institution)
all_players$Institution_and_State <- paste(all_players$Institution, all_players$State, sep = ", ")
all_players$Division <- as.character(all_players$Division)
# Conflating the divisions that end in BVB (the beach volleyball players that don't play the other kind) so we only have six divisions
all_players$Division <- ifelse(substr(all_players$Division, nchar(all_players$Division) - 2, nchar(all_players$Division)) == "BVB", 
                                      substr(all_players$Division, 1, nchar(all_players$Division) - 4), all_players$Division)

pr_shp <- read_sf('gz_2010_us_050_00_5m.json')
pr_shp_pr <- pr_shp[pr_shp$STATE == 72,]
centroids <- pr_shp_pr %>% 
    st_centroid() %>% 
    bind_cols(as_data_frame(st_coordinates(.)))    # unpack points to lat/lon columns

all_players_2 <- left_join(all_players, centroids, by = c('Hometown' = 'NAME'))
all_players_2 <- all_players_2[all_players_2$Hometown != "",]
all_players_2$Hometown.lon <- all_players_2$X
all_players_2$Hometown.lat <- all_players_2$Y
all_players_2[c("geometry", "GEO_ID", "STATE", "COUNTY", "LSAD", "CENSUSAREA", "X", "Y")] <- NULL


Institution_Coords <- geocode(all_players_2$Institution_and_State, source = "google")
# There's no way to turn off the messaging on the terminal, even if you use the "messaging = FALSE" option
all_players_2 <- cbind(all_players_2, Institution_Coords)
all_players_2$Institution.lon <- all_players_2$lon
all_players_2$Institution.lat <- all_players_2$lat
all_players_2[c("lon", "lat")] <- NULL
# For grouping the paths in ggplot
all_players_2$Player_Institution <- paste(all_players_2$Player, all_players_2$Institution, sep = " - ")


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

curves <- data.frame()
num_points = 20
for (idx in 1:nrow(all_players_2)) {
  curves <- rbind(curves, gcIntermediate(c(all_players_2$Hometown.lon[idx], all_players_2$Hometown.lat[idx]), c(all_players_2$Institution.lon[idx], all_players_2$Institution.lat[idx]), n=num_points, addStartEnd=TRUE))
  # df_cg_2_z <- cbind(df_cg_2, gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx]), n=20, addStartEnd=TRUE))
}


# https://stackoverflow.com/questions/29743691/duplicate-rows-in-a-data-frame-in-r
# 2nd answer
idx <- rep(1:nrow(all_players_2), rep(num_points + 2, nrow(all_players_2)))
all_players_3 <- all_players_2[idx,]
all_players_3_curves <- cbind(all_players_3, curves)

colors <- c("NAIA" = "#d52130", "NCAA DI" = "#005eb8", "NCAA DII" = "#005eb8", "NCAA DIII" = "#005eb8", "NJCAA DI" = "#1a4065", "NJCAA DII" = "#1a4065")

p <- ggplot(usa_shp_mainland_and_pr) + geom_sf(color = "white", fill = "light gray") + theme_map() + 
     geom_path(data = all_players_3_curves, aes(x=lon, y=lat, group=Player_Institution, color = Division)) + 
     scale_color_manual(values = colors)
     # geom_path(data = as.data.frame(inter), aes(x=lon, y=lat, group=NULL)) +
     # geom_path(data = as.data.frame(inter2), aes(x=lon, y=lat, group=NULL)) + 
     # geom_path(data = as.data.frame(inter3), aes(x=lon, y=lat, group=NULL))
print(p)