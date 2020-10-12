library(sf)
library(dplyr)
library(readr)
library(ggplot2)
library(geosphere)
library(ggmap)
library(extrafont)
register_google(key = "AIzaSyDV235gPhQgTX0_uHbxgCB5JqbdQkoj_L8")

# https://www.r-spatial.org/r/2018/10/25/ggplot2-sf.html
# http://dsgeek.com/2013/06/08/DrawingArcsonMaps.html
# https://flowingdata.com/2011/05/11/how-to-map-connections-with-great-circles/
# https://www.r-graph-gallery.com/how-to-draw-connecting-routes-on-map-with-r-and-great-circles.html

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
    legend.position = c(0.5, 0.975),
    legend.title = element_blank(),
    legend.spacing.x = unit(0.2, 'cm'),
    legend.text = element_text(size = 12),
    # panel.grid.minor = element_line(color = "#ebebe5", size = 0.2),
    panel.grid.major = element_line(color = "#ffffff", size = 0.2),
    plot.title = element_text(hjust = 0.5, colour = "steelblue4", size = 20),
    plot.subtitle = element_text(hjust = 0.5, vjust = -0.5, colour = "steelblue4", size = 14),
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
num_points = 30
for (idx in 1:nrow(all_players_2)) {
  curves <- rbind(curves, gcIntermediate(c(all_players_2$Hometown.lon[idx], all_players_2$Hometown.lat[idx]), c(all_players_2$Institution.lon[idx], all_players_2$Institution.lat[idx]), n=num_points, addStartEnd=TRUE))
  # df_cg_2_z <- cbind(df_cg_2, gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx]), n=20, addStartEnd=TRUE))
}

# https://stackoverflow.com/questions/29743691/duplicate-rows-in-a-data-frame-in-r
# 2nd answer
idx <- rep(1:nrow(all_players_2), rep(num_points + 2, nrow(all_players_2)))
all_players_3 <- all_players_2[idx,]
all_players_3_curves <- cbind(all_players_3, curves)

# https://stackoverflow.com/questions/15059093/ggplot2-adjust-the-symbol-size-in-legends
# https://stackoverflow.com/questions/11366964/is-there-a-way-to-change-the-spacing-between-legend-items-in-ggplot2
# https://stackoverflow.com/questions/16356052/control-ggplot2-legend-look-without-affecting-the-plot
line_df <- data.frame(x1 = -71, x2 = -68, y1 = 18.3, y2 = 18.3)
p <- ggplot(usa_shp_mainland_and_pr) + geom_sf(color = "white", fill = "light gray") + theme_map() + 
     geom_path(data = all_players_3_curves, aes(x=lon, y=lat, group=Player_Institution, color = Division)) + 
     guides(color = guide_legend(nrow = 1, override.aes = list(size = 2))) + 
     scale_color_brewer(palette="Set1") + 
     geom_label(x=-100, y=22, label="Each arc corresponds to a player and goes\nfrom her hometown to where she studies", size = 5, family = "Arial", color = "steelblue4", label.size = NA) +
     geom_segment(aes(x = x1, y = y1, xend = x2, yend = y2), colour = "steelblue4", data = line_df, arrow = arrow(length = unit(0.02, "npc"), type = "closed")) + 
     geom_label(x=-74, y=18.4, label="Puerto Rico", size = 4, family = "Arial", color = "steelblue4", label.size = NA) +
     ggtitle(label = "Puerto Rico Women Volleyball Players: Origins and Destinations", subtitle = "Academic Year 2019-2020")
print(p)

brewer.pal(6, "Set1")