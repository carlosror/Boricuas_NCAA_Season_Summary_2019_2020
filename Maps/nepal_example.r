library(sf)
library(dplyr)
library(readr)
library(ggplot2)

# https://stackoverflow.com/questions/50859765/chloropleth-map-with-geojson-and-ggplot2

nepal_shp <- read_sf('nepal-districts.geojson')
nepal_data <- read_csv('data.csv')

# calculate points at which to plot labels
centroids <- nepal_shp %>% 
    st_centroid() %>% 
    bind_cols(as_data_frame(st_coordinates(.)))    # unpack points to lat/lon columns

nepal_data2 <- filter(nepal_data, `Sub Group` == "HPI")
nepal_data2 <- mutate(nepal_data2, District = toupper(District))
nepal_data_join <- left_join(nepal_shp, nepal_data2, by = c('DISTRICT' = 'District'))

p <- ggplot(nepal_data_join) + geom_sf(aes(fill = Value)) + geom_text(aes(X, Y, label = DISTRICT), data = centroids, size = 1.5, color = 'white')
print(p)