library(ggplot2)
library(scales)
library(png)

fmu_df <- read.csv("FMU_record.csv", stringsAsFactors = FALSE)
w_2005_2014 <- sum(fmu_df$W[fmu_df$Year < 2015])
l_2005_2014 <- sum(fmu_df$L[fmu_df$Year < 2015])
wpctg_2005_2014 <- round(w_2005_2014 / (w_2005_2014 + l_2005_2014), 3)
row_2005_2014 <- as.data.frame(t(c("2005-2014", w_2005_2014 , l_2005_2014, wpctg_2005_2014)), stringsAsFactors = FALSE) # t for transpose
# https://stackoverflow.com/questions/3651198/r-insert-a-vector-as-a-row-in-data-frame
names(row_2005_2014) <- names(fmu_df)
row_2005_2014$W <- as.numeric(row_2005_2014$W)
row_2005_2014$L <- as.numeric(row_2005_2014$L)
row_2005_2014$Winning_Pctg <- as.numeric(row_2005_2014$Winning_Pctg)
fmu_df_2 <- rbind(row_2005_2014, fmu_df[fmu_df$Year > 2014,])
# highlight the 2019 season in the graph
fmu_df_2$Highlight <- ifelse(fmu_df_2$Year == 2019, "Yes", "No")
# https://stackoverflow.com/questions/45820250/highlight-a-single-bar-in-ggplot

FMU_champions <- readPNG("FMU_champions_2.png")
lion <- readPNG("./../../School_Logos/Florida_Memorial_University.png")
lion_2 <- readPNG("blue_lion.PNG")

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    axis.title.y = element_text(vjust=0, size = 15),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 12, angle = 0, vjust = 1, hjust = 0.5),
    axis.text.y = element_blank(), 
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_blank(),
    # panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(vjust = 10, size = 30), 
    plot.subtitle = element_text(vjust = 10, size = 15),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'gray95', color = "gray95"),
    plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}
# "#075EAB" "#FC8C38"
# using sprintf to control significant digits in plot's labels
# https://stackoverflow.com/questions/38369855/how-to-put-exact-number-of-decimal-places-on-label-ggplot-bar-chart
line_df <- data.frame(x1 = 5.6, x2 = 3.6, y1 = 0.6, y2 = 0.6)
p_fmu <- ggplot(fmu_df_2) + geom_bar(aes(x = Year, y = Winning_Pctg, fill = Highlight), stat = "identity", width = 0.4) +
         theme_plot() +
         ggtitle(label = "A Season for the Ages", subtitle = "After 14 consecutive losing seasons, the FMU Lions won \nThe Sun Conference Tournament Championship in 2019") +
         geom_text(aes(label = sprintf("%0.3f", round(Winning_Pctg, 3)), x = Year, y = Winning_Pctg), position = position_dodge(width = 0.75), vjust = -0.75, colour = "black", size = 4) + 
         ylab("Winning percentage") +
         ylim(0, 0.7) +
         scale_fill_manual( values = c( "Yes" = "#075EAB", "No" = "black" ), guide = FALSE ) +
         annotation_raster(FMU_champions, xmin = 0.7, xmax = 0.7 + 2.8, ymin = 0.325, ymax = 0.325 + 0.425) +
         annotation_raster(lion_2, xmin = 4.2, xmax = 4.2 + 2, ymin = 0.715, ymax = 0.715 + 0.3) +
         geom_segment(aes(x = x1, y = y1, xend = x2, yend = y2), colour = "Black", data = line_df, arrow = arrow(length = unit(0.02, "npc"), type = "closed")) +
         coord_cartesian(clip = "off")
print(p_fmu)

ggsave(plot = p_fmu, filename = "FMU_Barplot_2.png", width = 10.2, height = 10.2 * 572 / 868, device = "png", units = "in")