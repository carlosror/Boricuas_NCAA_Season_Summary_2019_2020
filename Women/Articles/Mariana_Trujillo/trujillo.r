library(ggplot2)
library(scales)
library(png)
library(reshape2) # melt

trujillo_df <- read.csv("Mariana_Trujillo_May_2019.csv", stringsAsFactors = FALSE)
# renaming a column which I can never remember
# https://stackoverflow.com/questions/7531868/how-to-rename-a-single-column-in-a-data-frame
names(trujillo_df)[names(trujillo_df) == "Running.Sets"] <- "Running Sets"
trujillo_df.m <- melt(trujillo_df[c("Date", "Running Sets", "Digs")], id.vars='Date')
# About that melt
# https://stackoverflow.com/questions/39061984/grouped-bar-chart-on-r-using-ggplot2

flag_names <- c("Chile", "Dominican_Republic", "Honduras", "Cuba", "Peru", "Guatemala", "Peru", "Chile", "Peru")
# flag_images = c()
# for (flag in flag_names) {
  # flag_images <- c(flag_images, readPNG(paste("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Country_flags/", flag , ".png", sep = "")))
# }
Flag_of_Chile <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Country_flags/Chile.png")
Flag_of_DR <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Country_flags/Dominican_Republic.png")
Flag_of_Honduras <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Country_flags/Honduras.png")
Flag_of_Cuba <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Country_flags/Cuba.png")
Flag_of_Guatemala <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Country_flags/Guatemala.png")
Flag_of_Peru <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Country_flags/Peru.png")

Trujillo <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Articles/Mariana_Trujillo/Mariana_Trujillo.png")

# Such a pain in the rear. I f I don't do this ggplot messes up the diacritical mark
# http://web.mit.edu/r/current/lib/R/library/base/html/Encoding.html
Peru <- "Perú"
Encoding(Peru) <- "UTF-8"
Mexico <- "México"
Encoding(Mexico) <- "UTF-8"

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    # axis.title.y = element_text(vjust=0, size = 15),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 12, angle = 0, vjust = 15, hjust = 0.5),
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
    legend.position = c(0.375,0.95),
    legend.title = element_blank(),
    legend.spacing.x = unit(0.2, 'cm'),
    legend.text = element_text(size = 12)
  )
}

# colorPalette <- c("#004FF0", "#EE0000") # Puerto Rico flag colors
colorPalette <- c("#4E2980", "#B6A368")
# p_trujillo <- ggplot(trujillo_df) + geom_bar(aes(x=Date, y = c(Running_Sets, Digs)), stat = "identity", fill = "red", width=0.4) + 
# p_trujillo <- ggplot(trujillo_df.m, aes(Date, value)) + geom_bar(aes(fill = variable), 
line_df <- data.frame(x1 = 7.5, x2 = 7.25, y1 = 31, y2 = 29)
line_df_2 <- data.frame(x1 = 1.55, x2 = 1.55, y1 = 32.5, y2 = 31)
p_trujillo <- ggplot(trujillo_df.m) + geom_bar(aes(x = Date, y = value, fill = variable),
     width = 0.5, position = position_dodge(width=0.5), stat="identity") +
     geom_text(aes(label = value, x = Date, y = value), position = position_dodge2(width = 0.5, preserve = "single"), vjust = -0.75, hjust = 0.5, colour = "black", size = 4) + 
     geom_rect(xmin = 7.6, xmax = 8.4, ymin = -0.7, ymax = 33, linetype = "dashed", fill = "white", color = "black", alpha = 0.00) +
     # scale_y_continuous(breaks = c(53), limits = c(0, 65)) +
     # geom_text(aes(label = max_kills, x=year, y = max_kills), position = position_dodge(width = 0.75), vjust = -0.6, size = 4) + 
     scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     guides(color = guide_legend(nrow = 1)) +
     ggtitle(label = "Two weeks in May", subtitle = "Setter Mariana Trujillo's busy second half of \nMay 2019 helped Puerto Rico qualify for the U18 Worlds") + 
     geom_vline(xintercept = 5.5, linetype = "dashed", size = 1.2, color = "gray") +
     geom_label(label = paste("U20 Pan American Cup\nLima, ", Peru), x = 0.70, y = 35, size = 4, hjust = "left") +
     geom_label(label = paste("U18 Pan American Cup\nDurango, ", Mexico), x = 5.7, y = 35, size = 4, hjust = "left") +
     annotation_raster(Flag_of_Chile, xmin = 0.75, xmax = 0.75 + 0.5, ymin = -5, ymax = -5 + 2.25) +
     annotation_raster(Flag_of_DR, xmin = 1.75, xmax = 1.75 + 0.5, ymin = -5, ymax = -5 + 2.25) +
     annotation_raster(Flag_of_Honduras, xmin = 2.75, xmax = 2.75 + 0.5, ymin = -5, ymax = -5 + 2) +
     annotation_raster(Flag_of_Cuba, xmin = 3.75, xmax = 3.75 + 0.5, ymin = -5, ymax = -5 + 2) +
     annotation_raster(Flag_of_Peru, xmin = 4.75, xmax = 4.75 + 0.5, ymin = -5, ymax = -5 + 2.25) +
     annotation_raster(Flag_of_Guatemala, xmin = 5.75, xmax = 5.75 + 0.5, ymin = -5, ymax = -5 + 2.25) +
     annotation_raster(Flag_of_Peru, xmin = 6.75, xmax = 6.75 + 0.5, ymin = -5, ymax = -5 + 2.25) +
     annotation_raster(Flag_of_Chile, xmin = 7.75, xmax = 7.75 + 0.5, ymin = -5, ymax = -5 + 2.25) +
     annotation_raster(Flag_of_Peru, xmin = 8.75, xmax = 8.75 + 0.5, ymin = -5, ymax = -5 + 2.25) +
     geom_segment(aes(x = x1, y = y1, xend = x2, yend = y2), colour = "Black", data = line_df, arrow = arrow(length = unit(0.02, "npc"), type = "closed")) +
     geom_label(x = 5.6, y = 27, label = "Puerto Rico beats Chile and\nqualifies for the U18 Worlds", size = 3.3, color = "Black", label.size = NA, hjust = "left") + 
     geom_segment(aes(x = x1, y = y1, xend = x2, yend = y2), colour = "Black", data = line_df_2, arrow = arrow(length = unit(0.02, "npc"), type = "closed")) +
     geom_label(x = 0.7, y = 30, label = "Trujillo named Best Setter", size = 3.3, color = "Black", label.size = NA, hjust = "left") + 
     geom_label(label = paste("Chile"), x = 1, y = -6.25, size = 3.5, label.size = NA) +
     geom_label(label = paste("Dominican\nRepublic"), x = 2, y = -7, size = 3.5, label.size = NA) +
     geom_label(label = paste("Honduras"), x = 3, y = -6.25, size = 3.5, label.size = NA) +
     geom_label(label = paste("Cuba"), x = 4, y = -6.25, size = 3.5, label.size = NA) +
     geom_label(label = paste(Peru), x = 5, y = -6.25, size = 3.5, label.size = NA) +
     geom_label(label = paste("Guatemala"), x = 6, y = -6.25, size = 3.5, label.size = NA) +
     geom_label(label = paste(Peru), x = 7, y = -6.25, size = 3.5, label.size = NA) +
     geom_label(label = paste("Chile"), x = 8, y = -6.25, size = 3.5, label.size = NA) +
     geom_label(label = paste(Peru), x = 9, y = -6.25, size = 3.5, label.size = NA) +
     annotation_raster(Trujillo, xmin = 8.45, xmax = 8.45 + 0.8, ymin = 40, ymax = 40 + 8.82) +
     # ylab("Assists in a match") + 
     # annotation_raster(eckert, xmin = 4.95, xmax = 5.45, ymin = 85, ymax = 111 ) + 
     # annotation_raster(aic_logo, xmin = 5.55, xmax = 6.25, ymin = 85, ymax = 111) + 
     coord_cartesian(clip = "off") + 
     ylim(-2, 35)  
print(p_trujillo)

ggsave(plot = p_trujillo, filename = "Trujillo_May_2019.png", width = 10.2, height = 10.2 * 722 / 952, device = "png", units = "in")