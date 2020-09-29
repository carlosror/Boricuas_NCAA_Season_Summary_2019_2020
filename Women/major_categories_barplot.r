library(ggplot2)
library(scales)
major_cats_df <- read.csv("major_cat_counts.csv")
theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    axis.title.y = element_text(vjust=4),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 11),
    axis.text.y = element_text(size = 14), 
    panel.grid.major.x = element_blank(),
    # panel.grid.major.y = element_blank(),
    panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(hjust = 1, vjust = 10, size = 15), 
    # plot.subtitle = element_text(hjust = -0.12, vjust = 10, , color = "orange"),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}

# Reorder major categories factor so that it plots the bars in the order I want
# https://stackoverflow.com/questions/5208679/order-bars-in-ggplot2-bar-graph
major_cats_df$Major_Cat <- factor(major_cats_df$Major_Cat, levels = c("Business", "Health and Medicine", "S.T.E.M.", "Social Sciences", "Other"))
colorPalette <- c("#173F5F", "#20639B", "#3CAEA3", "#F6D55C", "#ED553B")

p <- ggplot(major_cats_df) + geom_bar(aes(x=Major_Cat, y = PlayerCount, fill = Major_Cat), stat = "identity", width=0.5, position = position_dodge(width=0.8)) + 
     scale_y_continuous(limits = c(0, 60)) + 
     scale_fill_manual(values=colorPalette) +
     # geom_text(aes(label = paste(number_of_conferences, " / ", number_of_total_conferences), x=division, y = percent_of_conferences), position = position_dodge(width = 0.75), vjust = -0.6, colour = "cornflowerblue", size = 4) + 
     theme_plot() + 
     # theme(axis.title.x = element_blank(), axis.title.y = element_blank(), axis.ticks = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), text = element_text(size=16), plot.title = element_text(hjust = -0.3, vjust = 15), plot.margin = unit(c(2,1,1,1), "cm")) + 
     ggtitle(label = "Career fields pursued by women's volleyball student athletes from Puerto Rico") + 
     ylab("Number of students")
print(p)
ggsave(filename = "major_categories.png", width = 8, height = 4.3, device = "png", units = "in")