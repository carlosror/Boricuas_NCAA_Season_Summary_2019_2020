library(ggplot2)

source("write_csv_files.r")

NCAA_DI_TotalNum_Conf <- 32 # from NCAA_Division_1_volleyball_colleges spreadsheet
NCAA_DII_TotalNum_Conf <- 23 # from NCAA_Division_2_volleyball_colleges spreadsheet
NCAA_DIII_TotalNum_Conf <- 45 # from NCAA_Division_3_volleyball_colleges spreadsheet
NAIA_TotalNum_Conf <- 21 # from NAIA_volleyball_colleges_2019_2020 spreadsheet

NCAA_DI_Num_Conf <- length(unique(all_players$Conference[all_players$Division == "NCAA DI"]))
NCAA_DII_Num_Conf <- length(unique(all_players$Conference[all_players$Division == "NCAA DII"]))
NCAA_DIII_Num_Conf <- length(unique(all_players$Conference[all_players$Division == "NCAA DIII"]))
NAIA_Num_Conf <- length(unique(all_players$Conference[all_players$Division == "NAIA"]))

pcnt_conf_NCAA_DI <- NCAA_DI_Num_Conf / NCAA_DI_TotalNum_Conf
pcnt_conf_NCAA_DII <- NCAA_DII_Num_Conf / NCAA_DII_TotalNum_Conf
pcnt_conf_NCAA_DIII <- NCAA_DIII_Num_Conf / NCAA_DIII_TotalNum_Conf
pcnt_conf_NAIA <- NAIA_Num_Conf / NAIA_TotalNum_Conf

pcnt_conf <- c(pcnt_conf_NCAA_DI, pcnt_conf_NCAA_DII, pcnt_conf_NCAA_DIII, pcnt_conf_NAIA)

df_pcnt_conf <- data.frame(c("NCAA DI", "NCAA DII", "NCAA DIII", "NAIA"), pcnt_conf)
colnames(df_pcnt_conf) <- c("Division", "Percentage")

p_conf <- ggplot(data = df_pcnt_conf) + geom_bar(aes(x=Division, y=Percentage), stat="identity", fill = "dodgerblue4", width = 0.5) + 
     labs(x="", y = "") + ggtitle(label="Percentage of conferences with women players from Puerto Rico", subtitle = "Academic year 2019-2020") +
     scale_y_continuous(labels = scales::percent_format(accuracy = 1)) + theme_minimal() + 
     theme(plot.title = element_text(hjust = 0.5, size=20), plot.subtitle = element_text(hjust = 0.5, size = 14), axis.ticks = element_blank(), panel.grid.major.x = element_blank(), 
     axis.text=element_text(size=14)) 

NCAA_DI_TotalNum_Teams <- 334 # from NCAA_Division_1_volleyball_colleges spreadsheet
NCAA_DII_TotalNum_Teams <- 297 # from NCAA_Division_2_volleyball_colleges spreadsheet
NCAA_DIII_TotalNum_Teams <- 429 # from NCAA_Division_3_volleyball_colleges spreadsheet
NAIA_TotalNum_Teams <- 228 # from NAIA_volleyball_colleges_2019_2020 spreadsheet
NJCAA_DI_TotalNum_Teams <- 98 # from NJCAA_Division_1_volleyball_colleges_2019_2020 spreadsheet
NJCAA_DII_TotalNum_Teams <- 136 # from NJCAA_Division_2_volleyball_colleges_2019_2020 spreadsheet

NCAA_DI_Num_Teams <- length(unique(all_players$Institution[all_players$Division == "NCAA DI"]))
NCAA_DII_Num_Teams <- length(unique(all_players$Institution[all_players$Division == "NCAA DII"]))
NCAA_DIII_Num_Teams <- length(unique(all_players$Institution[all_players$Division == "NCAA DIII"]))
NAIA_Num_Teams <- length(unique(all_players$Institution[all_players$Division == "NAIA"]))
NJCAA_DI_Num_Teams <- length(unique(all_players$Institution[all_players$Division == "NJCAA DI"]))
NJCAA_DII_Num_Teams <- length(unique(all_players$Institution[all_players$Division == "NJCAA DII"]))

pcnt_teams_NCAA_DI <- NCAA_DI_Num_Teams / NCAA_DI_TotalNum_Teams
pcnt_teams_NCAA_DII <- NCAA_DII_Num_Teams / NCAA_DII_TotalNum_Teams
pcnt_teams_NCAA_DIII <- NCAA_DIII_Num_Teams / NCAA_DIII_TotalNum_Teams
pcnt_teams_NAIA <- NAIA_Num_Teams / NAIA_TotalNum_Teams
pcnt_teams_NJCAA_DI <- NJCAA_DI_Num_Teams / NJCAA_DI_TotalNum_Teams
pcnt_teams_NCAA_DII <- NJCAA_DII_Num_Teams / NJCAA_DII_TotalNum_Teams

pcnt_teams <- c(pcnt_teams_NCAA_DI, pcnt_teams_NCAA_DII, pcnt_teams_NCAA_DIII, pcnt_teams_NAIA, pcnt_teams_NJCAA_DI, pcnt_teams_NCAA_DII)
df_pcnt_teams <- data.frame(c("NCAA DI", "NCAA DII", "NCAA DIII", "NAIA", "NJCAA DI", "NJCAA DII"), pcnt_teams)
colnames(df_pcnt_teams) <- c("Division", "Percentage")

p_teams <- ggplot(data = df_pcnt_teams) + geom_bar(aes(x=Division, y=Percentage), stat="identity", fill = "dodgerblue4", width = 0.5) + 
     labs(x="", y = "") + ggtitle(label="Percentage of teams with women players from Puerto Rico", subtitle = "Academic year 2019-2020") +
     scale_y_continuous(labels = scales::percent_format(accuracy = 1)) + theme_minimal() + 
     theme(plot.title = element_text(hjust = 0.5, size=20), plot.subtitle = element_text(hjust = 0.5, size = 14), axis.ticks = element_blank(), panel.grid.major.x = element_blank(), 
     axis.text=element_text(size=14)) 