library(ggplot2)
library(scales)
dig_rankings <- read.csv("C:/Users/cesargb/Documents/Boricuas_NCAA/Season_Summary_2019_2020/Women/Lina_Bernier_Article/NCAA_DI_Digs_rankings_2019_2020.csv", stringsAsFactors = FALSE)
dig_rankings_500 <- dig_rankings[dig_rankings$Digs > 499,]
dig_rankings_500$Ht <- as.factor(dig_rankings_500$Ht)
# reorder so it displays heights in correct order
dig_rankings_500$Ht <- factor(dig_rankings_500$Ht, levels(dig_rankings_500$Ht)[c(1, 4:11, 2, 3)])
p <- ggplot(dig_rankings_500) + geom_bar(aes(x=Ht), fill="steelblue4", width=0.5, position = position_dodge(width=0.7)) 
     # scale_y_continuous(labels=percent) + 
     # geom_text(aes(label = paste(number_of_conferences, " / ", number_of_total_conferences), x=division, y = percent_of_conferences), position = position_dodge(width = 0.75), vjust = -0.6, colour = "cornflowerblue") + 
     # theme_minimal() + 
     # theme(axis.title.x = element_blank(), axis.title.y = element_blank(), axis.ticks = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), text = element_text(size=16), plot.title = element_text(hjust = -0.3, vjust = 15), plot.margin = unit(c(2,1,1,1), "cm")) + 
     # ggtitle(label = "Percentage of conferences with players from Puerto Rico by division")
print(p)
# base_plot + geom_bar(stat = "identity", fill=color_blind_palette[2],position = "dodge", width = 0.8) + geom_text(aes(label = paste("IGS =",Avg_IGS), x = Programa, y = count), position = position_dodge(width = 0.75), vjust = -0.6, colour = "red") 
