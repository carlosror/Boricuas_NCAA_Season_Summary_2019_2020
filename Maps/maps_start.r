library(geojsonio)
library(sp)
library(ggplot2)
library(dplyr)

spdf <- geojson_read("gz_2010_us_040_00_20m.json", what = "sp")
spdf_mainland = spdf[spdf@data$NAME != "Alaska" & spdf@data$NAME != "Puerto Rico" & spdf@data$NAME != "Hawaii",]
plot(spdf_mainland)

state_pop <- read.csv("State_Populations.csv")
state_pop2 <- rename(state_pop, region = State) 

state_pop2$region <- tolower(state_pop2$region)

states_map <- left_join(state_pop2, states, by = "region")
windows();
ggplot() + geom_polygon(data = states_map, aes( x = long, y = lat, group = group, fill=Population), color="grey") + theme_void() + coord_map()