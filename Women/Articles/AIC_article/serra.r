library(ggplot2)
library(scales)

Serra_stats_2018 <- read.csv("Andrea_Serra_stats_2018.csv")
Serra_stats_2019 <- read.csv("Andrea_Serra_stats_2019.csv")

year <- as.factor(c(2018, 2019))
max_kills <- c(max(Serra_stats_2018$K), max(Serra_stats_2019$K))
max_digs <- c(max(Serra_stats_2018$D), max(Serra_stats_2019$D))
max_aces <- c(max(Serra_stats_2018$SA), max(Serra_stats_2019$SA))

serra_df <- data.frame(year, max_kills, max_digs, max_aces)

theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    # axis.title.y = element_blank(),
    axis.title.y = element_text(vjust=8, size = 20),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 20),
    axis.text.y = element_text(size = 20), 
    panel.grid.major.x = element_blank(),
    # panel.grid.major.y = element_blank(),
    panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(hjust = 0.5, vjust = 10, size = 30), 
    # plot.subtitle = element_text(hjust = -0.12, vjust = 10, , color = "orange"),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}

colorPalette <- c("gray", "gold")
p_kills <- ggplot(serra_df) + geom_bar(aes(x=year, y = max_kills, fill = year), stat = "identity", width=0.4) +
     scale_y_continuous(breaks = c(0, 21, 31), limits = c(0, 33)) +
     # geom_text(aes(label = max_kills, x=year, y = max_kills), position = position_dodge(width = 0.75), vjust = -0.6, size = 4) + 
     scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     ggtitle(label = "Kills") + 
     ylab("Single-match high")
print(p_kills)

ggsave(plot = p_kills, filename = "serra_kills.png", width = 7, height = 7 * 722 / 959, device = "png", units = "in")

p_digs <- ggplot(serra_df) + geom_bar(aes(x=year, y = max_digs, fill = year), stat = "identity", width=0.4) +
     scale_y_continuous(breaks = c(0, 16, 28), limits = c(0, 30)) +
     scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     ggtitle(label = "Digs") + 
     ylab("Single-match high")
print(p_digs)

ggsave(plot = p_digs, filename = "serra_digs.png", width = 7, height = 7 * 722 / 959, device = "png", units = "in")

p_aces <- ggplot(serra_df) + geom_bar(aes(x=year, y = max_aces, fill = year), stat = "identity", width=0.4) +
     scale_y_continuous(breaks = c(0, 5, 9), limits = c(0, 11)) +
     scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     ggtitle(label = "Aces") + 
     ylab("Single-match high")
print(p_aces)

ggsave(plot = p_aces, filename = "serra_aces.png", width = 7, height = 7 * 722 / 959, device = "png", units = "in")