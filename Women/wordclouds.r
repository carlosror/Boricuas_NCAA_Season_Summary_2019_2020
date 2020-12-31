library(wordcloud2)
library(RColorBrewer)
# You have to play with it a bit
# *** Need to make sure the one with the highest frequency shows. If you make 'size' too large it won't ***
# For each of the "wordcloud" statements, maximize the Zoom window after you run it, 
# then clip it with Snipping Tool (IrfanView messes up the PNG's). Then fine tune the clipping 
# and rotate if necessary in GIMP.
source("write_csv_files.r")
df <- as.data.frame(table(all_players$Hometown))
colnames(df) <- c("hometown", "freq")
df2 <- as.data.frame(table(all_players$High_School[all_players$High_School_in_PR == "Y"]))
df3 <- as.data.frame(table(all_players$Institution))

# High schools wordcloud
colorVec_df2 = rep(brewer.pal(n=5, name = "Set1"), length.out=nrow(df2))
wordcloud2(df2, size = 0.4,color = colorVec_df2, rotateRatio = 0, minSize = 0.2)
# Institutions wordcloud
# After df3 wordcloud go to GIMP and rotate it
colorVec_df3 = rep(brewer.pal(n=5, name = "Set1"), length.out=nrow(df3))
wordcloud2(df3, size = 0.28,color = colorVec_df3, rotateRatio = 1, minRotation = pi/2, maxRotation = pi/2, minSize = 0.2)
# Hometowns wordcloud
colorVec_df = rep(brewer.pal(n=5, name = "Set1"), length.out=nrow(df))
wordcloud2(df, size = 1,color = colorVec_df, rotateRatio = 0, minSize = 0.2)