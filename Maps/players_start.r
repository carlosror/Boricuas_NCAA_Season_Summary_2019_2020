
ncaa1 <- read.csv("NCAA_Division_1_players_2019_2020_headers.csv", encoding = "UTF-8")
ncaa2 <- read.csv("NCAA_Division_2_players_2019_2020_headers.csv", encoding="UTF-8")
ncaa3 <- read.csv("NCAA_Division_3_players_2019_2020_headers.csv", encoding="UTF-8")
njcaa1 <- read.csv("NJCAA_Division_1_players_2019_2020_headers.csv", encoding="UTF-8")
njcaa2 <- read.csv("NJCAA_Division_2_players_2019_2020_headers.csv", encoding="UTF-8")
naia <- read.csv("NAIA_players_2019_2020_headers.csv", encoding="UTF-8")

all_players <- rbind(ncaa1, ncaa2, ncaa3, njcaa1, njcaa2, naia)