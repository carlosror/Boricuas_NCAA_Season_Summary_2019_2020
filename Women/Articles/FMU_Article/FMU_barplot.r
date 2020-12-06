library(ggplot2)
library(scales)
library(png)

fmu_df <- read.csv("FMU_record.csv", stringsAsFactors = FALSE)
w_2005_2014 <- sum(fmu_df$W[fmu_df$Year < 2015])
l_2005_2014 <- sum(fmu_df$L[fmu_df$Year < 2015])
wpctg_2005_2014 <- w_2005_2014 / (w_2005_2014 + l_2005_2014)
row_2005_2014 <- as.data.frame(t(c("2005-2014", w_2005_2014 , l_2005_2014, wpctg_2005_2014)), stringsAsFactors = FALSE) # t for transpose
# https://stackoverflow.com/questions/3651198/r-insert-a-vector-as-a-row-in-data-frame
names(row_2005_2014) <- names(fmu_df)
fmu_df_2 <- rbind(row_2005_2014, fmu_df[fmu_df$Year > 2014,])

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
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}

p_fmu <- ggplot(fmu_df_2) + geom_bar(aes(x = Year, y = Winning_Pctg), stat = "identity", fill = "#075EAB") +
         theme_plot()
         
print(p_fmu)