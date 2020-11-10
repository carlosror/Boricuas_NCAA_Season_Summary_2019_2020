library(ggplot2)
library(scales)
library(png)

Vital_stats <- read.csv("Vianca_Vital_Stats_2019.csv", stringsAsFactors = FALSE)

num_times_50_plus_assists <- length(Vital_stats$A[Vital_stats$A > 49])
num_times_20_plus_digs <- length(Vital_stats$D[Vital_stats$D > 19])
num_times_4_plus_aces <- length(Vital_stats$SA[Vital_stats$SA > 3])

numbers <- c(num_times_50_plus_assists, num_times_20_plus_digs, num_times_4_plus_aces)
categories <- c("50+ assists", "20+ digs", "4+ aces")

vital_df <- data.frame(categories, numbers)

# Re-ordering dates:
vital_df$categories <- factor(vital_df$categories, levels(vital_df$categories)[c(3,1,2)])

# eckert <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Articles/AIC_article_2019_2020/Naomi_Eckert.png")
# aic_logo <- readPNG("./../../School_Logos/American_International_College.png")

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    axis.title.y = element_text(vjust=0, size = 15),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 15, vjust = 0, hjust = 0.5),
    axis.text.y = element_blank(), 
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_blank(),
    # panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(vjust = 10, size = 20), 
    plot.subtitle = element_text(vjust = 10, size = 15),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}

colorPalette <- c("gray", "gold")
p <- ggplot(vital_df) + geom_bar(aes(x=categories, y = numbers), stat = "identity", fill = "firebrick", width=0.4) + 
     geom_text(aes(label = numbers, x = categories, y = numbers), position = position_dodge(width = 0.75), vjust = -0.75, colour = "black", size = 7) + 
     # scale_y_continuous(breaks = c(53), limits = c(0, 65)) +
     # geom_text(aes(label = numbers, x=year, y = max_kills), position = position_dodge(width = 0.75), vjust = -0.6, size = 4) + 
     # scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     ggtitle(label = "Vianca Vital: By the numbers", subtitle = "Academic Year 2019-2020") + 
     ylab("Number of matches") + 
     # annotation_raster(eckert, xmin = 4.95, xmax = 5.45, ymin = 85, ymax = 111 ) + 
     # annotation_raster(aic_logo, xmin = 5.55, xmax = 6.25, ymin = 85, ymax = 111) + 
     coord_cartesian(clip = "off") +
     ylim(0, 4.5)
print(p)

# ggsave(plot = p_assists, filename = "eckert_assists.png", width = 11, height = 11 * 537 / 1018, device = "png", units = "in")