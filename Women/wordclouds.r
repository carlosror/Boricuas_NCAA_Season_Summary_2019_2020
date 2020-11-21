library(wordcloud2)
# You have to play with it a bit
source("write_csv_files.r")
df <- as.data.frame(table(all_players$Hometown))
colnames(df) <- c("hometown", "freq")
df2 <- as.data.frame(table(all_players$High_School[all_players$High_School_in_PR == "Y"]))
df3 <- as.data.frame(table(all_players$Institution))

# High schools wordcloud
wordcloud2(df2, size = 0.45,color = "random-dark", rotateRatio = 0, minSize = 0.2)
# Institutions wordcloud
# After df3 wordcloud go to GIMP and rotate it
wordcloud2(df3, size = 0.28,color = "random-dark", rotateRatio = 1, minRotation = pi/2, maxRotation = pi/2, minSize = 0.2)
# Hometowns wordcloud
wordcloud2(df, size = 1.3,color = "random-dark", rotateRatio = 0, minSize = 0.2)