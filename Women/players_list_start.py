#!/usr/bin/env python
# -*- coding: utf-8 -*-

players_list = []
with open("NCAA_Division_2_players_2019_2020.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    full_name = current_line_list[0].split()
    first_name = full_name[0]
    first_last_name = full_name[1]
    if (full_name[1] == "de"): 
      image_filename = "./NCAA_DII_mugshots/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
      player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
    else:
      image_filename = "./NCAA_DII_mugshots/" + first_name + "_" + first_last_name + ".jpg"
      player_name = first_name + " " + first_last_name
    cl_pos_ht = current_line_list[1] + " | " + current_line_list[2] + " | " + current_line_list[3]
    hometown = current_line_list[6]
    single_player_list = [image_filename, player_name, cl_pos_ht, hometown]
    players_list.append(single_player_list)
print(players_list)

