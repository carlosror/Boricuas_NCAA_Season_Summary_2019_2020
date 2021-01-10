library(ggplot2)
library(scales)
library(png)
library(extrafont)
dig_rankings <- read.csv("NCAA_DI_Digs_rankings_2019_2020.csv", stringsAsFactors = FALSE)
dig_rankings_500 <- dig_rankings[dig_rankings$Digs > 499,]
dig_rankings_500$Height <- dig_rankings_500$Ht
dig_rankings_500$Ht <- NULL
dig_rankings_500$Height <- as.factor(dig_rankings_500$Height)
# reorder so it displays heigHeights in correct order
dig_rankings_500$Height <- factor(dig_rankings_500$Height, levels(dig_rankings_500$Height)[c(1, 4:11, 2, 3)])

bernier_photo <- readPNG("Lina_Bernier_10_cropped_2.png")
bernier <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Articles/Lina_Bernier_Article/Lina_Bernier.png")
fiu_logo <- readPNG("./../../School_Logos/Florida_International_University.png")

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    # axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    # axis.title.y = element_blank(),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 12, vjust = 4),
    axis.text.y = element_text(size = 14), 
    axis.title.x = element_text(vjust=2, size = 12),
    axis.title.y = element_text(vjust=4, size = 12),
    panel.grid.major.x = element_blank(),
    # panel.grid.major.y = element_blank(),
    panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(hjust = 0.0, vjust = 8, size = 20), 
    plot.subtitle = element_text(hjust = 0.0, vjust = 5, size = 12),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}
# How to place an image in a categorical plot using annotation_raster
# https://stackoverflow.com/questions/59276040/r-how-to-use-categorical-variables-to-set-limit-for-image-insertion
# To draw an arrow:
# https://stackoverflow.com/questions/15059093/ggplot2-adjust-the-symbol-size-in-legends
# https://stackoverflow.com/questions/11366964/is-there-a-way-to-change-the-spacing-between-legend-items-in-ggplot2
# https://stackoverflow.com/questions/16356052/control-ggplot2-legend-look-without-affecting-the-plot
line_df <- data.frame(x1 = 11, x2 = 10.8, y1 = 1.2, y2 = 2.8)
p <- ggplot(dig_rankings_500) + geom_bar(aes(x=Height), fill="steelblue4", width=0.5, position = position_dodge(width=0.7)) + 
     scale_y_continuous(breaks = c(1, 10, 20), limits = c(0, 22)) + 
     xlab("Height") +  ylab("Number of players with 500+ digs, by height") + 
     annotation_raster(raster = bernier_photo, xmin = 9.5, xmax = 11.5, ymin = 3, ymax = 23) + 
     # annotation_raster(raster = bernier, xmin = 9, xmax = 9.8, ymin = 24, ymax = 29) +
     coord_cartesian(clip = "off") + 
     theme_plot() + 
     ggtitle(label = "Standing Tall", subtitle = "At 5-11, FIU's Lina Bernier was the tallest player with 500+ digs in NCAA Division I in 2019") + 
     geom_label(x = 8.2, y = 19, label = "Lina Bernier", size = 7, family = "Playball", color = "Black", label.size = NA) + 
     geom_label(x = 9.2, y = 16.3, label = "530 digs\n5.15 digs/set", size = 5, color = "Black", label.size = NA, hjust = "right") +
     geom_segment(aes(x = x1, y = y1, xend = x2, yend = y2), colour = "Black", data = line_df, arrow = arrow(length = unit(0.02, "npc"), type = "closed"))
     # theme_plot()
     # scale_y_continuous(labels=percent) + 
     # geom_text(aes(label = paste(number_of_conferences, " / ", number_of_total_conferences), x=division, y = percent_of_conferences), position = position_dodge(width = 0.75), vjust = -0.6, colour = "cornflowerblue") + 
     # theme_minimal() + 
     # theme(axis.title.x = element_blank(), axis.title.y = element_blank(), axis.ticks = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), text = element_text(size=16), plot.title = element_text(hjust = -0.3, vjust = 15), plot.margin = unit(c(2,1,1,1), "cm")) + 
     # ggtitle(label = "Percentage of conferences with players from Puerto Rico by division")
print(p)

ggsave(plot = p, filename = "Bernier_heights_2.png", width = 9.5, height = 9.5 * 627 / 925, device = "png", units = "in")