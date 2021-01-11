library(ggplot2)
library(scales)
library(png)

Eckert_stats <- read.csv("Naomi_Eckert_Stats_2019.csv", stringsAsFactors = FALSE)

dates <- Eckert_stats$Date[Eckert_stats$A > 52]
assists <- Eckert_stats$A[Eckert_stats$A > 52]

eckert_df <- data.frame(dates, assists)
# eckert_df$dates <- as.Date(as.character(eckert_df$dates), "%m/%d/%y")
# Re-ordering dates:
eckert_df$dates <- factor(eckert_df$dates, levels(eckert_df$dates)[c(4:6, 1:3)])

eckert <- readPNG("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Articles/AIC_article_2019_2020/Naomi_Eckert.png")
aic_logo <- readPNG("./../../School_Logos/American_International_College.png")

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    axis.title.y = element_text(vjust=0, size = 15),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 12, angle = 45, vjust = 1, hjust = 1),
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
    legend.position = "none"
  )
}

colorPalette <- c("gray", "gold")
p_assists <- ggplot(eckert_df) + geom_bar(aes(x=dates, y = assists), stat = "identity", fill = "gold", width=0.4) + 
     geom_text(aes(label = assists, x = dates, y = assists), position = position_dodge(width = 0.75), vjust = -0.75, colour = "black", size = 7) + 
     # scale_y_continuous(breaks = c(53), limits = c(0, 65)) +
     # geom_text(aes(label = max_kills, x=year, y = max_kills), position = position_dodge(width = 0.75), vjust = -0.6, size = 4) + 
     # scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     ggtitle(label = "New kid on the block", subtitle = "Naomi Eckert topped the single-match AIC \nfreshman record for assists at least 6 times in 2019") + 
     ylab("Assists in a match") + 
     annotation_raster(eckert, xmin = 4.95, xmax = 5.45, ymin = 85, ymax = 111 ) + 
     annotation_raster(aic_logo, xmin = 5.55, xmax = 6.25, ymin = 85, ymax = 111) + 
     coord_cartesian(clip = "off") + 
     ylim(0, 70)
print(p_assists)

ggsave(plot = p_assists, filename = "eckert_assists.png", width = 11, height = 11 * 537 / 1018, device = "png", units = "in")