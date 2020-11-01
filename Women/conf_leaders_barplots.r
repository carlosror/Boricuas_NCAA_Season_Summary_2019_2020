library(ggplot2)

conf_leaders <- read.csv("Conference_leaders.csv", encoding = "UTF-8")
# unique_leaders <- unique(conf_leaders[c("Player_Name", "Division", "Position")])

conf_leaders$Category <- as.character(conf_leaders$Category)
conf_leaders$Category2 <- ifelse(conf_leaders$Category == "aces/set", "aces",
                                      ifelse(conf_leaders$Category == "assists/set", "assists",
                                      ifelse(conf_leaders$Category == "digs/set", "digs",
                                      ifelse(conf_leaders$Category == "kills/set" | conf_leaders$Category == "points" | conf_leaders$Category == "points/set", "kills",
                                      ifelse(conf_leaders$Category == "blocks/set", "blocks",
                                      ifelse(conf_leaders$Category == "blocks/set", "blocks", conf_leaders$Category
                                      ))))))

unique_leaders <- unique(conf_leaders[c("Player_Name", "Division", "Position")])
theme_plot <- function(...) {
  # theme_minimal() +
  theme( 
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    # axis.title.y = element_text(vjust=4),
    axis.ticks = element_blank(),
    axis.text.x = element_text(size = 15),
    axis.text.y = element_text(size = 15), 
    panel.grid.major.x = element_blank(),
    # panel.grid.major.y = element_blank(),
    panel.grid.major.y = element_line(colour = "gray75"),
    panel.grid.minor = element_blank(), 
    # text = element_text(size=16), 
    plot.title = element_text(hjust = 0.5, vjust = 10, size = 20), 
    # plot.subtitle = element_text(hjust = -0.12, vjust = 10, , color = "orange"),
    plot.margin = unit(c(2,1,1,1), "cm"),
    panel.background = element_rect(fill = 'white', color = "white"),
    # plot.background = element_rect(fill = 'gray95'),
    panel.border = element_blank(),
    legend.position = "none"
  )
}

colorPalette <- c("#d52130", "#005eb8", "#005eb8", "#005eb8", "#1a4065", "#1a4065")

p <- ggplot(unique_leaders) + geom_bar(aes(x=Division, fill = Division), stat = "count", width=0.5, position = position_dodge(width=0.7)) + 
     ylim(0, 25) + 
     scale_fill_manual(values=colorPalette) +
     theme_plot() + 
     ggtitle(label = "Number of conference leaders by division")
     
q <- ggplot(unique_leaders) + geom_bar(aes(x=Position), fill = "steelblue4", stat = "count", width=0.5, position = position_dodge(width=0.7)) + 
     theme_plot() + 
     ggtitle(label = "Number of conference leaders by position")
     
r <- ggplot(conf_leaders) + geom_bar(aes(x=Category2), fill = "steelblue4", stat = "count", width=0.5, position = position_dodge(width=0.7)) + 
     theme_plot() + 
     ggtitle(label = "Number of conference leaders by statistical category")