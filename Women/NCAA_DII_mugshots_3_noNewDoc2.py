#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
import time
margins = (36, 36, 0, 0)

players_list = []
with open("NCAA_Division_1_players_2019_2020.csv") as f:
  next(f)
  for line in f:
    current_line_list = line.split(",")
    full_name = current_line_list[0].split()
    first_name = full_name[0]
    first_last_name = full_name[1]
    if (full_name[1] == "de" or full_name[1] == "La"): 
      image_filename = "./NCAA_DI_mugshots_2/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
      player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
    else:
      image_filename = "./NCAA_DI_mugshots_2/" + first_name + "_" + first_last_name + ".jpg"
      player_name = first_name + " " + first_last_name
    cl_pos_ht = current_line_list[1] + " | " + current_line_list[2] + " | " + current_line_list[3]
    hometown = current_line_list[6]
    single_player_list = [image_filename, player_name, cl_pos_ht, hometown]
    players_list.append(single_player_list)


defineColor("NJCAA Blue", 217, 168, 55, 94)
defineColor("NJCAA Gray", 0, 0, 0, 40)
  
top_rect = createRect(0, 0, 612, 36)
setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
bottom_rect = createRect(0, 756, 612, 36)
setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
center_rect = createRect(0, 36, 612, 720)
setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)

pic_x_coord = 36; pic_y_coord = 42
num_players = len(players_list)
mugshot_w = 96
mugshot_h = 128
num_rows = 4; num_cols = 5
row_sum_start = 0
if (num_players % 20) == 0: 
  num_pages = (num_players / 20) 
else: 
  num_pages = (num_players / 20) + 1
player_count = 0
for page in range(1, num_pages + 1):
  start = time.time()
  page_header = createText(36, 9, 540, 36)
  setText("NCAA Division II Players Snapshots", page_header)
  setTextColor("White", page_header)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
  setTextAlignment(ALIGN_CENTERED, page_header)
  for row in range(1, num_rows + 1):
    row_sum = 4 * (row - 1) 
    for col in range(1, num_cols + 1):
      mugshot = createImage(pic_x_coord, pic_y_coord, mugshot_w, mugshot_h)
      idx = row * col + row_sum - 1 + 20 * (page - 1)
      loadImage(players_list[idx][0], mugshot)
      setScaleImageToFrame(1, 1, mugshot)
  
      player_name_text_height = 11
      player_hometown_text_height = 13
      mugshot_text = createText(pic_x_coord, pic_y_coord + mugshot_h + 5, mugshot_w, player_name_text_height)
      insertText(players_list[idx][1] + "\n", -1, mugshot_text)
      insertText(players_list[idx][2] + "\n", -1, mugshot_text)
      name_class_length = getTextLength(mugshot_text)
      setFont("Asimov Print C", mugshot_text); setFontSize(player_name_text_height - 2, mugshot_text)
      player_hometowm = players_list[idx][3]
      insertText(player_hometowm + "\n", -1, mugshot_text)
      selectText(name_class_length, len(player_hometowm), mugshot_text)
      setFont("Playball Regular", mugshot_text); # setFontSize(player_hometown_text_height - 2, mugshot_text)
      setTextColor("NJCAA Blue", mugshot_text)
      setTextAlignment(ALIGN_CENTERED, mugshot_text)
        
        # setFont("Asimov Print C", mugshot_text_name); setFontSize(player_name_text_height - 2, mugshot_text_name)
        # setTextColor("NJCAA Blue", mugshot_text_name)
        # setTextAlignment(ALIGN_CENTERED, mugshot_text_name)
    
        # player_class_text_height = 11
        # mugshot_text_class = createText(pic_x_coord, pic_y_coord + mugshot_h + 5 + player_name_text_height, mugshot_w, player_class_text_height)
        # setText(players_list[idx][2] + "\n", mugshot_text_class)
        # setFont("Asimov Print C", mugshot_text_class); setFontSize(player_class_text_height - 2, mugshot_text_class)
        # setTextColor("NJCAA Blue", mugshot_text_class)
        # setTextAlignment(ALIGN_CENTERED, mugshot_text_class)
    
        # player_hometown_text_height = 13
        # mugshot_text_hometown = createText(pic_x_coord, pic_y_coord + mugshot_h + 5 + player_name_text_height + player_class_text_height , mugshot_w, player_hometown_text_height)
        # setText(players_list[idx][3] + "\n", mugshot_text_hometown)
        # setFont("Playball Regular", mugshot_text_hometown); setFontSize(player_hometown_text_height - 2, mugshot_text_hometown)
        # setTextColor("NJCAA Blue", mugshot_text_hometown)
        # setTextAlignment(ALIGN_CENTERED, mugshot_text_hometown)
        
      player_count += 1
      if player_count == num_players: 
        end = time.time()
        page_time = str(end - start)
        page_debug = createText(576, 756, 36, 36)
        setText(page_time, page_debug)
        exit()
    
      pic_x_coord += 111
      row_sum -= row - 1
    pic_y_coord += 180
    pic_x_coord = 36
    #row_sum += 4
  end = time.time()
  page_time = str(end - start)
  page_debug = createText(576, 756, 36, 36)
  setText(page_time, page_debug)
  newPage(-1)
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
  pic_x_coord = 36; pic_y_coord = 42