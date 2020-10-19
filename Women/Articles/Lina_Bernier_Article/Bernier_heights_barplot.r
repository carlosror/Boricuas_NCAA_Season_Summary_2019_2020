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

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    # axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    axis.title.y = element_blank(),
    axis.ticks.x = element_blank(),
    axis.text.x = element_text(size = 12, vjust = 4),
    axis.text.y = element_text(size = 14), 
    panel.grid.major.x = element_blank(),
    # panel.grid.major.y = element_blank(),
    panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(hjust = 0.5, vjust = 10, size = 20), 
    plot.subtitle = element_text(hjust = 0.5, vjust = 5, size = 14),
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
line_df <- data.frame(x1 = 11, x2 = 10.5, y1 = 1.2, y2 = 4)
p <- ggplot(dig_rankings_500) + geom_bar(aes(x=Height), fill="steelblue4", width=0.5, position = position_dodge(width=0.7)) + 
     scale_y_continuous(breaks = c(1, 10, 20), limits = c(0, 20)) + 
     xlab("Height") +  
     annotation_raster(raster = bernier_photo, xmin = 9, xmax = 11, ymin =6, ymax = 19) +
     theme_plot() + 
     ggtitle(label = "The tallest of them all", subtitle = "Number of players with 500+ digs in NCAA Division I, by height\nAcademic Year 2019-2020") + 
     geom_label(x = 9.8, y = 5, label = "Lina Bernier", size = 7, family = "Playball", color = "Black", label.size = NA) + 
     geom_label(x = 9.2, y = 18, label = "530 digs\n5.15 digs/set", size = 5, color = "Black", label.size = NA, hjust = "right") +
     geom_segment(aes(x = x1, y = y1, xend = x2, yend = y2), colour = "Black", data = line_df, arrow = arrow(length = unit(0.02, "npc"), type = "closed"))
     # theme_plot()
     # scale_y_continuous(labels=percent) + 
     # geom_text(aes(label = paste(number_of_conferences, " / ", number_of_total_conferences), x=division, y = percent_of_conferences), position = position_dodge(width = 0.75), vjust = -0.6, colour = "cornflowerblue") + 
     # theme_minimal() + 
     # theme(axis.title.x = element_blank(), axis.title.y = element_blank(), axis.ticks = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), text = element_text(size=16), plot.title = element_text(hjust = -0.3, vjust = 15), plot.margin = unit(c(2,1,1,1), "cm")) + 
     # ggtitle(label = "Percentage of conferences with players from Puerto Rico by division")
print(p)
# base_plot + geom_bar(stat = "identity", fill=color_blind_palette[2],position = "dodge", width = 0.8) + geom_text(aes(label = paste("IGS =",Avg_IGS), x = Programa, y = count), position = position_dodge(width = 0.75), vjust = -0.6, colour = "red") 
