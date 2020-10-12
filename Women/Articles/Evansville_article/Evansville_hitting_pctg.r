library(ggplot2)
library(extrafont)
library(png)

# Such a pain in the rear. I f I don't do this ggplot messes up the á in Vázquez
# http://web.mit.edu/r/current/lib/R/library/base/html/Encoding.html
Vazquez <- "Vázquez"
Encoding(Vazquez) <- "UTF-8"

evansville <- read.csv("Evansville_article/Vazquez_and_Feliciano.csv", nrows = 30)
evansville_logo <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/School_Logos/University_of_Evansville.png")
feliciano <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Evansville_article/Melanie_Feliciano.png")
vazquez <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Evansville_article/Alondra_Vazquez.png")

theme_plot <- function(...) {
  theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.ticks = element_blank(),
    axis.text.x = element_blank(),
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_blank(),
    # panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    text = element_text(size=16), 
    plot.title = element_text(hjust = -0.065, vjust = 12.5, face = "bold", color = "orange"), 
    plot.subtitle = element_text(hjust = -0.12, vjust = 10, , color = "orange"),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'gray95', color = "gray95"),
    plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank()
  )
}


p <- ggplot(data=evansville, aes(x=c(1:30), y=Combined_Hitting_Pctg)) + geom_line(size=1.2, color = "purple") + geom_point(size = 3, color = "purple") + 
     geom_text(aes(label = Match_Result, x=c(1:30), y=Combined_Hitting_Pctg), position = position_dodge(width = 0.75), vjust = -1.5, colour = "orange", fontface = "bold") + 
     theme_plot() + 
     scale_y_continuous(labels = scales::percent_format(accuracy = 1), limits = c(0.0, 0.5), breaks = c(0.0, 0.21, 0.45)) + 
     # geom_label(label = paste("It pays to be efficient\nFeliciano's and", Vazquez, "' combined hitting % and match outcomes"), x = 8, y = 0.45, size = 5) 
     ggtitle(label = "It pays to be efficient", subtitle = paste("Feliciano's and ", Vazquez, "' combined hitting % and match outcomes", sep = "")) +
     geom_hline(yintercept = 0.21, linetype = "dashed", size = 1.5, color = "gray75") + geom_hline(yintercept = 0.0, color = "gray 75") + geom_hline(yintercept = 0.45, color = "gray 75") + 
     geom_text(x=10, y=0.48, label="9-3", size = 14, family = "OLD SPORT 02 ATHLETIC NCV", color = "orange") + 
     annotate(geom = "text", x=10, y=0.41, label = "Aces record\nwhen duo hits\n21% or higher", color = "orange") + 
     geom_text(x=16, y=0.48, label="23.1%", size = 14, family = "OLD SPORT 02 ATHLETIC NCV", color = "orange") + 
     annotate(geom = "text", x=16, y=0.435, label = "Duo's hitting % in wins", color = "orange") + 
     geom_text(x=22, y=0.48, label="16.2%", size = 14, family = "OLD SPORT 02 ATHLETIC NCV", color = "orange") + 
     annotate(geom = "text", x=22, y=0.435, label = "Duo's hitting % in losses", color = "orange") + 
     annotation_raster(feliciano, xmin = 24, xmax = 26, ymin = 0.55, ymax = 0.55 + 0.115) + 
     annotation_raster(vazquez, xmin = 26.5, xmax = 28.5, ymin = 0.55, ymax = 0.55 + 0.115) + 
     annotation_raster(evansville_logo, xmin = 29, xmax = 31.7, ymin = 0.55, ymax = 0.55 + 0.115) + 
     # annotation_raster(evansville_logo, xmin = 25, xmax = 27, ymin = 0.55, ymax = 0.6) + 
     coord_cartesian(clip = "off") 
          
print(p)