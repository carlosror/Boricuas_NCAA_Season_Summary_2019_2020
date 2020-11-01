library(ggplot2)

all_players_500_digs_heights <- read.csv("./../../all_players_500_digs_heights.csv", encoding = "UTF-8")

# The following is just so that I can plot "5-9" and "5-10", since there are players from PR of those those heights with 500+ digs 
heights_count <- table(all_players_500_digs_heights$Height)
heights_count["5-9"] <- 0
heights_count["5-10"] <- 0
heights_count_df <- as.data.frame(cbind(heights_count))
heights_count_df$heights <- rownames(heights_count_df)
heights_count_df$heights <- as.factor(heights_count_df$heights)
heights_count_df$heights <- factor(heights_count_df$heights, levels(heights_count_df$heights)[c(1:2, 5:12, 3:4)])

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
# line_df <- data.frame(x1 = 11, x2 = 10.5, y1 = 1.2, y2 = 4)
p <- ggplot(heights_count_df) + geom_bar(aes(x=heights, y = heights_count), stat = "identity", fill="steelblue4", width=0.5, position = position_dodge(width=0.7)) + 
     scale_y_continuous(breaks = c(1, 5), limits = c(0, 5)) + 
     xlab("Height") +  
     theme_plot() + 
     ggtitle(label = "Heights of players from Puerto Rico with 500+ digs", subtitle = "All Divisions\nAcademic Year 2019-2020")
     # theme_plot()
     # scale_y_continuous(labels=percent) + 
     # geom_text(aes(label = paste(number_of_conferences, " / ", number_of_total_conferences), x=division, y = percent_of_conferences), position = position_dodge(width = 0.75), vjust = -0.6, colour = "cornflowerblue") + 
     # theme_minimal() + 
     # theme(axis.title.x = element_blank(), axis.title.y = element_blank(), axis.ticks = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), text = element_text(size=16), plot.title = element_text(hjust = -0.3, vjust = 15), plot.margin = unit(c(2,1,1,1), "cm")) + 
     # ggtitle(label = "Percentage of conferences with players from Puerto Rico by division")
print(p)
# base_plot + geom_bar(stat = "identity", fill=color_blind_palette[2],position = "dodge", width = 0.8) + geom_text(aes(label = paste("IGS =",Avg_IGS), x = Programa, y = count), position = position_dodge(width = 0.75), vjust = -0.6, colour = "red") 
