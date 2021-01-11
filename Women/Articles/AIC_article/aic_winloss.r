library(ggplot2)
library(extrafont) # Tyoe "fonts()" to see fonts available. Only works with TrueType fonts
library(png)
aic_winloss <- read.csv("AIC_record_2019_2020.csv")
aic_logo <- readPNG("./../../School_Logos/American_International_College.png")
aic_team <- readPNG("AIC_team.png")

theme_plot <- function(...) {
  theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    axis.title.y = element_text(size = 12, vjust = 5),
    axis.ticks = element_blank(),
    axis.text.x = element_blank(),
    panel.grid.major.x = element_blank(), 
    panel.grid.minor = element_blank(), 
    text = element_text(size=16), 
    plot.title = element_text(hjust = 0.5, vjust = 15), 
    plot.subtitle = element_text(hjust = 0.5, vjust = 10),
    plot.margin = unit(c(2,1,1,1), "cm"),
    # panel.background = element_rect(fill = 'gray100', color = "gray95"),
    # plot.background = element_rect(fill = 'gray100'),
    panel.border = element_blank()
  )
}

p <- ggplot(data=aic_winloss, aes(x=c(1:31), y=Winning_Pctg)) + geom_line(size=1.2, color = "gold") + geom_point(size = 3) + 
     geom_text(aes(label = Result, x=c(1:31), y=Winning_Pctg), position = position_dodge(width = 0.75), vjust = -0.6, colour = "black", fontface = "bold") + 
     theme_plot() + 
     # ggtitle(label = "A Season in Two Acts", subtitle = "AIC's 2019-2020 volleyball season") + 
     scale_y_continuous(labels = scales::number_format(accuracy = 0.001)) + 
     geom_vline(xintercept = 16, linetype = "dashed", size = 1.2, color = "gray") + 
     geom_rect(xmin = 0, xmax = 15.9, ymin = -0.1, ymax = 0.5, fill = "gray95", alpha = 0.05) + 
     geom_text(x=3, y=0.22, label="2-14", size = 14, family = "Pink Sans") + 
     # geom_text(x=6, y=0.275, label="through first\n16 matches", size = 6, family = "Arial Narrow") + 
     #geom_text(x=25, y=0.275, label="through first\n16 matches", size = 6, family = "Arial Narrow", colour="black") + 
     annotate(geom = "text", x=3, y=0.175, label = "through first\n16 matches") +
     geom_text(x=9, y=0.22, label="0.192", size = 14, family = "Pink Sans") + 
     annotate(geom = "text", x=9, y=0.175, label = "opponents\nhitting %") + 
     geom_text(x=24, y=0.32, label="12-3", size = 14, family = "Pink Sans", color = "black") + 
     annotate(geom = "text", x=24, y=0.275, label = "in final\n15 matches", color = "black") +
     geom_text(x=30, y=0.32, label="0.125", size = 14, family = "Pink Sans", color = "black") + 
     annotate(geom = "text", x=30, y=0.275, label = "opponents\nhitting %", color = "black") + 
     geom_text(x=27, y=0.22, label="14-5", size = 14, family = "Pink Sans", color = "black") + 
     annotate(geom = "text", x=27, y=0.175, label = "overall record\nwhen opponents\nhitting % < 0.180", color = "black") + 
     geom_label(label = "A Season in Two Acts\nAIC's 2019-2020 volleyball season", x = 6, y = 0.45, size = 7) + 
     annotation_raster(aic_logo, ymin = 0.405,ymax= 0.405 + 0.0717,xmin = 17.5,xmax = 20.5) + 
     annotation_raster(aic_team, ymin = -0.02,ymax= -0.02 + 0.1505,xmin = 23.5,xmax = 30.5) + 
     ylab("Winning Percentage")
     
print(p)