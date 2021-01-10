library(ggplot2)
library(scales)

Fuentes_stats_df <- read.csv("Andrea_Fuentes_stats_2018_2019.csv")

Fuentes_stats_df$year <- as.factor(Fuentes_stats_df$year)

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    # axis.title.y = element_text(vjust=8, size = 14),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 25),
    axis.text.y = element_text(size = 25), 
    panel.grid.major.x = element_blank(),
    # panel.grid.major.y = element_blank(),
    panel.grid.major.y = element_line(colour = "gray55"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(hjust = 0.5, vjust = 10, size = 35), 
    # plot.subtitle = element_text(hjust = -0.12, vjust = 10, , color = "orange"),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = '#F1B82D', color = "#F1B82D"),
    plot.background = element_rect(fill = "#F1B82D", color = "#F1B82D"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none",
  )
}

colorPalette <- c("gray", "black")
p_assists_per_set <- ggplot(Fuentes_stats_df) + geom_bar(aes(x=year, y = assists_per_set, fill = year), stat = "identity", width=0.4) +
     scale_y_continuous(breaks = c(0, 8.69, 11.77), limits = c(0, 12)) +
     # geom_text(aes(label = max_kills, x=year, y = max_kills), position = position_dodge(width = 0.75), vjust = -0.6, size = 4) + 
     scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     ggtitle(label = "Assists per set") 
     # ylab("Single-match high")
print(p_assists_per_set)

p_missouri_hit_pcntg <- ggplot(Fuentes_stats_df) + geom_bar(aes(x=year, y = team_hit_pcntg, fill = year), stat = "identity", width=0.4) +
     scale_y_continuous(breaks = c(0.20, 0.263, 0.301), limits = c(0.205, 0.305), oob = rescale_none) +
     # geom_text(aes(label = max_kills, x=year, y = max_kills), position = position_dodge(width = 0.75), vjust = -0.6, size = 4) + 
     scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     ggtitle(label = "Missouri hitting percentage") 
     # ylab("Single-match high")
print(p_missouri_hit_pcntg)

ggsave(plot = p_assists_per_set, filename = "p_assists_per_set.png", width = 9.5, height = 9.5 * 722 / 959, device = "png", units = "in")
ggsave(plot = p_missouri_hit_pcntg, filename = "p_missouri_hit_pcntg.png", width = 9.5, height = 9.5 * 722 / 959, device = "png", units = "in")
