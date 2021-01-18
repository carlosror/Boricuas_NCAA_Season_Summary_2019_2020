library(ggplot2)
library(scales)
library(png)
library(reshape2) # melt

hitting_df <- read.csv("Hitting_Pctg.csv", stringsAsFactors = FALSE)
hitting_df$Year <- as.factor(hitting_df$Year)
Hollingsworth <- readPNG("Dariana_Hollingsworth_21_cutout.png")
Omazic <- readPNG("Tyanna_Omazic_7_cutout.png")
Deberg <- readPNG("Kylie_Deberg_cutout.png")

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    axis.title.y = element_text(vjust=0, size = 15),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 12),
    axis.text.y = element_blank(), 
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_blank(),
    # panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(vjust = 10, size = 30), 
    plot.subtitle = element_text(vjust = 10, size = 15),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = c(0.8, 1.15),
    legend.title = element_blank(),
    legend.spacing.x = unit(0.2, 'cm'),
    legend.text = element_text(size = 12),
    legend.direction = "horizontal"
  )
}

# colorPalette <- c("#858788", "#F1B82D")
colorPalette <- c("black", "#F1B82D")
# colorPalette <- c("gray", "black")
p_httg <- ggplot(hitting_df) + 
     geom_bar(aes(x = Player, y = Httg_Pctg, fill = Year), width = 0.5, position = position_dodge(width=0.5), stat="identity") +
     geom_text(aes(label = Httg_Pctg, x = Player, y = Httg_Pctg), position = position_dodge2(width = 0.5, preserve = "single"), vjust = -0.75, hjust = 0.5, colour = "black", size = 4) + 
     scale_fill_manual(values=alpha(colorPalette, 1.0)) +
     ggtitle(label = "Three Effective Tigers", subtitle = "Hollingsworth, Deberg, and Omazic saw their\nhitting percentage numbers skyrocket in 2019") +
     ylab("Hitting %") +
     guides(colour = guide_legend(nrow = 1)) +
     coord_cartesian(clip = "off") +
     ylim(0, 0.4) +
     annotation_raster(Hollingsworth, xmin = 0.70, xmax = 0.7 + 0.60, ymin = 0.0, ymax = 0.0 + 0.2) + 
     annotation_raster(Omazic, xmin = 2.8, xmax = 2.8 + 0.60, ymin = -0.007, ymax = -0.007 + 0.24) + 
     annotation_raster(Deberg, xmin = 1.6, xmax = 1.6 + 0.8, ymin = 0.0, ymax = 0.0 + 0.222) + 
     theme_plot()
print(p_httg)
ggsave(plot = p_httg, filename = "Hitting_Pctg.png", width = 10.2, height = 10.2 * (32 / 54), device = "png", units = "in")