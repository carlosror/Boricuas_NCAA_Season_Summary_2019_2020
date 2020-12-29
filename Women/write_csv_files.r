ncaa1 <- read.csv("NCAA_Division_1_players_2019_2020.csv", encoding = "UTF-8")
ncaa2 <- read.csv("NCAA_Division_2_players_2019_2020.csv", encoding="UTF-8")
ncaa3 <- read.csv("NCAA_Division_3_players_2019_2020.csv", encoding="UTF-8")
njcaa1 <- read.csv("NJCAA_Division_1_players_2019_2020.csv", encoding="UTF-8")
njcaa2 <- read.csv("NJCAA_Division_2_players_2019_2020.csv", encoding="UTF-8")
naia <- read.csv("NAIA_players_2019_2020.csv", encoding="UTF-8")
bvb <- read.csv("NCAA_NJCAA_NAIA_beach_volleyball_players_2019_2020.csv", encoding="UTF-8")
# bvb$Position <- rep("", dim(bvb)[1]) # adding blanks for beach vb players' Position
# so I can concatenate the rows (rbind)

# You cannot use the dupliacted() function here because 2 players might have the same name.
# For example, in 2019-2020 there were 2 Claudis Rivera's: one in Tampa, the other in Massachusetts.
# First, concatenate all the datasets except the beach volleyball one using rbind()
# Second, subset the beach volleyball dataset to include only those that play beach vb and *not* floor vb
# Then concatenate the two resulting datasets from steps 1 and 2
all_players_no_bvb <- rbind(naia, ncaa1, ncaa2, ncaa3, njcaa1, njcaa2)
players_bvb_only <- bvb[!(bvb$Player %in% all_players_no_bvb$Player),]

all_players <- rbind(all_players_no_bvb, players_bvb_only)

# Converting the vectors I want to sort by from factors to characters
# It does something weird with the ordering if left as factors
all_players$Hometown <- as.character(all_players$Hometown)
all_players$Institution <- as.character(all_players$Institution)

write.csv(all_players, file = "all_players.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")

write.csv(all_players[order(all_players$Hometown, all_players$Institution),], 
          file = "all_players_order_municip.csv", row.names = FALSE, 
          quote = FALSE, fileEncoding = "UTF-8")

all_players_PR_High_School <- all_players[all_players$High_School_in_PR == "Y",]

all_players_PR_High_School$High_School <- as.character(all_players_PR_High_School$High_School)

write.csv(all_players_PR_High_School[order(all_players_PR_High_School$High_School, all_players_PR_High_School$Institution),], 
          file = "all_players_order_high_school.csv", row.names = FALSE, 
          quote = FALSE, fileEncoding = "UTF-8")
          
player_counts <- as.data.frame(table(all_players$Hometown), col.names = c("Pueblo", "PlayerCount"))
colnames(player_counts) <- c("Hometown", "PlayerCount")
player_counts$Hometown <- as.character(player_counts$Hometown)
player_counts <- player_counts[order(player_counts$Hometown),]
write.csv(player_counts, file = "player_counts_muni.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")

player_counts_states <- as.data.frame(table(all_players$State), col.names = c("State", "PlayerCount"))
colnames(player_counts_states) <- c("State", "PlayerCount")
player_counts_states$State <- as.character(player_counts_states$State)
player_counts_states <- player_counts_states[order(player_counts_states$State),]
player_counts_states$State[player_counts_states$State == "Washington, D.C."] <- "Washington D.C."
write.csv(player_counts_states, file = "player_counts_states.csv", row.names = FALSE, quote = FALSE)

# Player stats:

ncaa1_stats <- read.csv("NCAA_Division_1_players_2019_2020_Statistics.csv", encoding = "UTF-8")
ncaa2_stats <- read.csv("NCAA_Division_2_players_2019_2020_Statistics.csv", encoding="UTF-8")
ncaa3_stats <- read.csv("NCAA_Division_3_players_2019_2020_Statistics.csv", encoding="UTF-8")
njcaa1_stats <- read.csv("NJCAA_Division_1_players_2019_2020_Statistics.csv", encoding="UTF-8")
njcaa2_stats <- read.csv("NJCAA_Division_2_players_2019_2020_Statistics.csv", encoding="UTF-8")
naia_stats <- read.csv("NAIA_players_2019_2020_Statistics.csv", encoding="UTF-8")

all_players_stats <- rbind(ncaa1_stats, ncaa2_stats, ncaa3_stats, njcaa1_stats, njcaa2_stats, naia_stats)
all_players_stats$Division <- as.character(all_players_stats$Division)
# all_players_stats$Stat_link <- NULL

club_400_kills <- all_players_stats[all_players_stats$K > 399 & !is.na(all_players_stats$K),]
club_300_kills_300_digs <- all_players_stats[all_players_stats$K > 299 & all_players_stats$D > 299 &  !is.na(all_players_stats$K) & !is.na(all_players_stats$D),]
club_500_digs <- all_players_stats[all_players_stats$D > 499 & !is.na(all_players_stats$D),]
club_800_assists_300_digs <- all_players_stats[all_players_stats$A > 799 & all_players_stats$D > 299 &  !is.na(all_players_stats$A) & !is.na(all_players_stats$D),]
club_60_aces <- all_players_stats[all_players_stats$SA > 59 & !is.na(all_players_stats$SA),]
club_60_blocks <- all_players_stats[all_players_stats$TOT > 59 & !is.na(all_players_stats$TOT),]
club_900_assists <- all_players_stats[all_players_stats$A > 899 & !is.na(all_players_stats$A),]
club_200_kills_200_assists_200_digs <- all_players_stats[all_players_stats$K > 199 & !is.na(all_players_stats$K) & all_players_stats$D > 199 & all_players_stats$A > 199 ,]

write.csv(club_400_kills[order(club_400_kills$Division),], file = "club_400_kills.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")
write.csv(club_300_kills_300_digs[order(club_300_kills_300_digs$Division),], file = "club_300_kills_300_digs.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")
write.csv(club_500_digs[order(club_500_digs$Division),], file = "club_500_digs.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")
write.csv(club_800_assists_300_digs[order(club_800_assists_300_digs$Division),], file = "club_800_assists_300_digs.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")
write.csv(club_60_aces[order(club_60_aces$Division),], file = "club_60_aces.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")
write.csv(club_60_blocks[order(club_60_blocks$Division),], file = "club_60_blocks.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")
write.csv(club_900_assists[order(club_900_assists$Division),], file = "club_900_assists.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")
write.csv(club_200_kills_200_assists_200_digs[order(club_200_kills_200_assists_200_digs$Division),], file = "club_200_kills_200_assists_200_digs.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")
# For Bernier article
all_players_500_digs <- all_players_stats[all_players_stats$D > 499 & !is.na(all_players_stats$D),]
all_players_500_digs_heights <- merge(all_players_500_digs, all_players[c("Player", "Height")], by = "Player")
write.csv(all_players_500_digs_heights, file = "all_players_500_digs_heights.csv", row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")

## Table of % of conferences with Puerto Rican players in them, by division

all_players$Conference <- as.character(all_players$Conference)
NAIA_total_conf <- 20 # From NAIA_Conferences spreadsheet
NCAA_DI_total_conf <- 32 # From NCAA_Division_1_Conferences spreadsheet and verified with Wikipedia
NCAA_DII_total_conf <- 24 # From NCAA_Division_2_Conferences spreadsheet and verified with Wikipedia
NCAA_DIII_total_conf <- 44 # From NCAA_Division_3_Conferences spreadsheet and verified with Wikipedia
NJCAA_DI_total_conf <- 20 # manually counted from https://www.njcaa.org/sports/wvball/teams-page
NJCAA_DII_total_conf <- 17 # manually counted from https://www.njcaa.org/sports/wvball/teams-page

# NAIA
NAIA_num_conf <- length(unique(all_players$Conference[all_players$Division == "NAIA"]))
NAIA_pct_conf <- round(NAIA_num_conf / NAIA_total_conf, 3)

# NCAA DI
NCAA_DI_num_conf <- length(unique(all_players$Conference[all_players$Division == "NCAA DI"]))
NCAA_DI_pct_conf <- round(NCAA_DI_num_conf / NCAA_DI_total_conf, 3)

# NCAA DII
NCAA_DII_num_conf <- length(unique(all_players$Conference[all_players$Division == "NCAA DII"]))
NCAA_DII_pct_conf <- round(NCAA_DII_num_conf / NCAA_DII_total_conf, 3)

# NCAA DIII
NCAA_DIII_num_conf <- length(unique(all_players$Conference[all_players$Division == "NCAA DIII"]))
NCAA_DIII_pct_conf <- round(NCAA_DIII_num_conf / NCAA_DIII_total_conf, 3)

# NJCAA DI
NJCAA_DI_num_conf <- length(unique(all_players$Conference[all_players$Division == "NJCAA DI"]))
NJCAA_DI_pct_conf <- round(NJCAA_DI_num_conf / NJCAA_DI_total_conf, 3)

# NJCAA DII
NJCAA_DII_num_conf <- length(unique(all_players$Conference[all_players$Division == "NJCAA DII"]))
NJCAA_DII_pct_conf <- round(NJCAA_DII_num_conf / NJCAA_DII_total_conf, 3)

# Writing the table of conferences with Puerto Rican players in them, by division
division <- c("NAIA", "NCAA DI", "NCAA DII", "NCAA DIII", "NJCAA DI", "NJCAA DII")
number_of_conferences <- c(NAIA_num_conf, NCAA_DI_num_conf, NCAA_DII_num_conf, NCAA_DIII_num_conf, NJCAA_DI_num_conf, NJCAA_DII_num_conf)
number_of_total_conferences <- c(NAIA_total_conf, NCAA_DI_total_conf, NCAA_DII_total_conf, NCAA_DIII_total_conf, NJCAA_DI_total_conf, NJCAA_DII_total_conf)
percent_of_conferences <- c(NAIA_pct_conf, NCAA_DI_pct_conf, NCAA_DII_pct_conf, NCAA_DIII_pct_conf, NJCAA_DI_pct_conf, NJCAA_DII_pct_conf)
pcnt_conf_df <- as.data.frame(cbind(division, number_of_conferences, number_of_total_conferences, percent_of_conferences))
write.csv(pcnt_conf_df, file = "conference_pctgs.csv", row.names = FALSE, quote = FALSE)

# Generating tables by division of teams with the most Puerto Rican players
# There's probably a more efficient way to do it :|
team_counts_NAIA <- sort(table(all_players$Institution[all_players$Division == "NAIA"]), decreasing = TRUE)[1:10]
team_counts_NAIA <- as.data.frame(team_counts_NAIA)
colnames(team_counts_NAIA) <- c("Institution", "PlayerCount")
write.csv(team_counts_NAIA, file = "team_counts_NAIA.csv", row.names = FALSE, quote = FALSE)

team_counts_NCAA_DI <- sort(table(all_players$Institution[all_players$Division == "NCAA DI"]), decreasing = TRUE)[1:10]
team_counts_NCAA_DI <- as.data.frame(team_counts_NCAA_DI)
colnames(team_counts_NCAA_DI) <- c("Institution", "PlayerCount")
write.csv(team_counts_NCAA_DI, file = "team_counts_NCAA_DI.csv", row.names = FALSE, quote = FALSE)

team_counts_NCAA_DII <- sort(table(all_players$Institution[all_players$Division == "NCAA DII"]), decreasing = TRUE)[1:10]
team_counts_NCAA_DII <- as.data.frame(team_counts_NCAA_DII)
colnames(team_counts_NCAA_DII) <- c("Institution", "PlayerCount")
write.csv(team_counts_NCAA_DII, file = "team_counts_NCAA_DII.csv", row.names = FALSE, quote = FALSE)

team_counts_NCAA_DIII <- sort(table(all_players$Institution[all_players$Division == "NCAA DIII"]), decreasing = TRUE)[1:10]
team_counts_NCAA_DIII <- as.data.frame(team_counts_NCAA_DIII)
colnames(team_counts_NCAA_DIII) <- c("Institution", "PlayerCount")
write.csv(team_counts_NCAA_DIII, file = "team_counts_NCAA_DIII.csv", row.names = FALSE, quote = FALSE)

team_counts_NJCAA_DI <- sort(table(all_players$Institution[all_players$Division == "NJCAA DI"]), decreasing = TRUE)[1:10]
team_counts_NJCAA_DI <- as.data.frame(team_counts_NJCAA_DI)
colnames(team_counts_NJCAA_DI) <- c("Institution", "PlayerCount")
write.csv(team_counts_NJCAA_DI, file = "team_counts_NJCAA_DI.csv", row.names = FALSE, quote = FALSE)

team_counts_NJCAA_DII <- sort(table(all_players$Institution[all_players$Division == "NJCAA DII"]), decreasing = TRUE)[1:10]
team_counts_NJCAA_DII <- as.data.frame(team_counts_NJCAA_DII)
colnames(team_counts_NJCAA_DII) <- c("Institution", "PlayerCount")
write.csv(team_counts_NJCAA_DII, file = "team_counts_NJCAA_DII.csv", row.names = FALSE, quote = FALSE)

###########################
# Table of major categories
###########################

all_players$Major_Category <- as.character(all_players$Major_Category)
# Merging Arts and Humanities and other major categories
all_players$Major_Category2 <- ifelse(all_players$Major_Category == "Arts and Humanities" | 
                                      all_players$Major_Category == "Interdisciplinary Studies" | 
                                      all_players$Major_Category == "Public and Social Services", 
                                      "Other", all_players$Major_Category)

# Writing table of player counts for each major category
major_cat_counts <- sort(table(all_players$Major_Category2[all_players$Major_Category2 != "" & !is.na(all_players$Major_Category2)]), decreasing = TRUE)
major_cat_counts <- as.data.frame(major_cat_counts)
colnames(major_cat_counts) <- c("Major_Cat", "PlayerCount")
write.csv(major_cat_counts, file = "major_cat_counts.csv", row.names = FALSE, quote = FALSE)

# Writing table of player counts for S.T.E.M. majors
major_counts_STEM <- sort(table(all_players$Major[all_players$Major_Category2 == "S.T.E.M."]), decreasing = TRUE)[1:5]
major_counts_STEM <- as.data.frame(major_counts_STEM)
colnames(major_counts_STEM) <- c("Major", "PlayerCount")
write.csv(major_counts_STEM, file = "major_counts_STEM.csv", row.names = FALSE, quote = FALSE)

# Writing table of player counts for Health majors
major_counts_Health <- sort(table(all_players$Major[all_players$Major_Category2 == "Health and Medicine"]), decreasing = TRUE)[1:5]
major_counts_Health <- as.data.frame(major_counts_Health)
colnames(major_counts_Health) <- c("Major", "PlayerCount")
write.csv(major_counts_Health, file = "major_counts_Health_and_Medicine.csv", row.names = FALSE, quote = FALSE)

# Writing table of player counts for Social Sciences majors
major_counts_Social <- sort(table(all_players$Major[all_players$Major_Category2 == "Social Sciences"]), decreasing = TRUE)[1:5]
major_counts_Social <- as.data.frame(major_counts_Social)
colnames(major_counts_Social) <- c("Major", "PlayerCount")
write.csv(major_counts_Social, file = "major_counts_Social_Sciences.csv", row.names = FALSE, quote = FALSE)

# Writing table of player counts for Business majors
major_counts_Business <- sort(table(all_players$Major[all_players$Major_Category2 == "Business"]), decreasing = TRUE)[1:5]
major_counts_Business <- as.data.frame(major_counts_Business)
colnames(major_counts_Business) <- c("Major", "PlayerCount")
write.csv(major_counts_Business, file = "major_counts_Business.csv", row.names = FALSE, quote = FALSE)

# Writing table of player counts for Other majors
major_counts_Other <- sort(table(all_players$Major[all_players$Major_Category2 == "Other"]), decreasing = TRUE)[1:5]
major_counts_Other <- as.data.frame(major_counts_Other)
colnames(major_counts_Other) <- c("Major", "PlayerCount")
write.csv(major_counts_Other, file = "major_counts_Other.csv", row.names = FALSE, quote = FALSE)