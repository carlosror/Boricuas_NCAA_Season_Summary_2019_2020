library(sf)
library(dplyr)
library(readr)
library(ggplot2)
library(geosphere)

usa_shp <- read_sf('gz_2010_us_040_00_20m.json')
usa_shp_mainland_and_pr <- usa_shp[usa_shp$NAME != "Alaska" & usa_shp$NAME != "Hawaii",]

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

lat_ca <- 39.164141
lon_ca <- -121.640625
lat_me <- 45.213004
lon_me <- -68.906250
lon_pr <- -66.0156
lat_pr <- 18.4278
df_cg <- data.frame(c(lon_ca, lon_pr, lon_me), c(lat_ca, lat_pr, lat_me), c(lon_pr, lon_me, lon_ca), c(lat_pr, lat_me, lat_ca))
names(df_cg) <- c("p1_lon", "p1_lat", "p2_lon", "p2_lat")
df_cg$name <- c("CA_to_PR", "PR_to_ME", "ME_to_CA")

z <- data.frame()
# df_cg_2_z <- df_cg_2
for (idx in 1:nrow(df_cg)) {
  z <- rbind(z, gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx]), n=20, addStartEnd=TRUE))
  # df_cg_2_z <- cbind(df_cg_2, gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx]), n=20, addStartEnd=TRUE))
}

# df_cg_2 <- df_cg[rep(1:3, 22),]
# df_cg_2 <- rbind(df_cg[rep(1,22),], df_cg[rep(2,22),], df_cg[rep(3,22),])

# https://stackoverflow.com/questions/29743691/duplicate-rows-in-a-data-frame-in-r
# 2nd answer
idx <- rep(1:nrow(df_cg), rep(22, nrow(df_cg)))
df_cg_2 <- df_cg[idx,]
df_cg_2_z <- cbind(df_cg_2, z)
inter <- gcIntermediate(c(lon_ca, lat_ca), c(lon_me, lat_me), n=20, addStartEnd=TRUE)
inter2 <- gcIntermediate(c(lon_ca, lat_ca), c(lon_pr, lat_pr), n=20, addStartEnd=TRUE)
inter3 <- gcIntermediate(c(lon_pr, lat_pr), c(lon_me, lat_me), n=20, addStartEnd=TRUE)

p <- ggplot(usa_shp_mainland_and_pr) + geom_sf(color = "white", fill = "light gray") + theme_map() + 
     geom_path(data = df_cg_2_z, aes(x=lon, y=lat, group=name, color = name))
     # geom_path(data = as.data.frame(inter), aes(x=lon, y=lat, group=NULL)) +
     # geom_path(data = as.data.frame(inter2), aes(x=lon, y=lat, group=NULL)) + 
     # geom_path(data = as.data.frame(inter3), aes(x=lon, y=lat, group=NULL))
print(p)