library(ggplot2)
library(scales)
pcnt_conf_df <- read.csv("conference_pctgs.csv")
theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 12),
    axis.text.y = element_text(size = 14), 
    panel.grid.major.x = element_blank(),
    # panel.grid.major.y = element_blank(),
    panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(hjust = 0, vjust = 10, size = 16), 
    # plot.subtitle = element_text(hjust = -0.12, vjust = 10, , color = "orange"),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}

colorPalette <- c("#d52130", "#005eb8", "#005eb8", "#005eb8", "#1a4065", "#1a4065")

p <- ggplot(pcnt_conf_df) + geom_bar(aes(x=division, y = percent_of_conferences, fill = division), stat = "identity", width=0.5, position = position_dodge(width=0.7)) + 
     scale_y_continuous(labels = scales::percent_format(accuracy = 1), limits = c(0.0, 0.65)) + 
     scale_fill_manual(values=colorPalette) +
     geom_text(aes(label = paste(number_of_conferences, " / ", number_of_total_conferences), x=division, y = percent_of_conferences), position = position_dodge(width = 0.75), vjust = -0.6, colour = "cornflowerblue", size = 4) + 
     theme_plot() + 
     # theme(axis.title.x = element_blank(), axis.title.y = element_blank(), axis.ticks = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), text = element_text(size=16), plot.title = element_text(hjust = -0.3, vjust = 15), plot.margin = unit(c(2,1,1,1), "cm")) + 
     ggtitle(label = "Percentage of conferences with players from Puerto Rico by division")
print(p)
ggsave(filename = "conference_pctgs_chart.png", width = 8, height = 4.3, device = "png", units = "in")