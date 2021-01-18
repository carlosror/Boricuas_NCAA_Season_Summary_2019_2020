library(ggplot2)
library(scales)
library(png)

missouri_df <- read.csv("Missouri_seasons.csv", stringsAsFactors = FALSE)
# highlight the 1990's period in the graph
missouri_df$Highlight <- ifelse(missouri_df$Period == "1990's", "Black", ifelse(missouri_df$Period == "2000 - 2018", "Gray", "Gold"))
# https://stackoverflow.com/questions/45820250/highlight-a-single-bar-in-ggplot

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    axis.title.y = element_text(vjust=0, size = 15),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 14, angle = 0, vjust = 1, hjust = 0.5),
    axis.text.y = element_blank(), 
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_blank(),
    # panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(vjust = 10, size = 25), 
    plot.subtitle = element_text(vjust = 8, size = 15),
    plot.margin = unit(c(2,1,1.5,1), "cm"),
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}
# "#075EAB" "#FC8C38"
# using sprintf to control significant digits in plot's labels
# https://stackoverflow.com/questions/38369855/how-to-put-exact-number-of-decimal-places-on-label-ggplot-bar-chart
# line_df <- data.frame(x1 = 5.6, x2 = 3.6, y1 = 0.6, y2 = 0.6)
p_missouri <- ggplot(missouri_df) + geom_bar(aes(x = Period, y = Winning_Pctg, fill = Highlight), stat = "identity", width = 0.4) +
         theme_plot() +
         ggtitle(label = "Three Tiger Eras", subtitle = "The nineties, the Kreklows, and the Taylors") +
         geom_text(aes(label = sprintf("%0.3f", round(Winning_Pctg, 3)), x = Period, y = Winning_Pctg), position = position_dodge(width = 0.75), vjust = -0.75, colour = "black", size = 6) + 
         geom_label(x = 2, y = -0.14, label = "The Kreklows", size = 5, label.size = NA) +
         geom_label(x = 3, y = -0.14, label = "The Taylors", size = 5, label.size = NA) +
         ylab("Winning %") +
         ylim(0, 0.8) +
         scale_fill_manual( values = c( "Black" = "black", "Gray" = "gray75", "Gold" = "#F1B82D" ), guide = FALSE ) +
         # annotation_raster(FMU_champions, xmin = 0.7, xmax = 0.7 + 2.8, ymin = 0.325, ymax = 0.325 + 0.425) +
         # annotation_raster(lion_2, xmin = 4.2, xmax = 4.2 + 2, ymin = 0.715, ymax = 0.715 + 0.3) +
         # geom_segment(aes(x = x1, y = y1, xend = x2, yend = y2), colour = "Black", data = line_df, arrow = arrow(length = unit(0.02, "npc"), type = "closed")) +
         coord_cartesian(clip = "off")
print(p_missouri)

ggsave(plot = p_missouri, filename = "Missouri_seasons.png", width = 10.2, height = 10.2 * 572 / 868, device = "png", units = "in")