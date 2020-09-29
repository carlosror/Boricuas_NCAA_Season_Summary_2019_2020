#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
import time
margins = (36, 36, 0, 0)

escuelas_dict = {}
with open("./Escuelas/filesizes_png.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    escuelas_dict[current_line_list[0]] = float(current_line_list[2]) / float (current_line_list[1])
    
escuelas_cities_dict = {}
with open("./High_School_Cities.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    escuelas_cities_dict[current_line_list[0]] = current_line_list[1]

escuela_dict = {}
with open("./all_players_order_high_school.csv") as f:
  next(f) # skip the headers
  for line in f:
    current_line_list = line.split(",")
    if current_line_list[7] == "": continue
    full_name = current_line_list[0].split()
    first_name = full_name[0]
    first_last_name = full_name[1]
    if (full_name[1] == "de" or full_name[1] == "La"): 
      image_filename = "./" + current_line_list[14].replace(" ", "_").replace("\n", "") + "_thumbs/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
      player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
    else:
      image_filename = "./" + current_line_list[14].replace(" ", "_").replace("\n", "") + "_thumbs/" + first_name + "_" + first_last_name + ".jpg"
      player_name = first_name + " " + first_last_name
    college = current_line_list[10]
    college_state = current_line_list[11]
    if college_state == "Washington D.C.": college_state = "Washington, D.C."
    single_player_list = [image_filename, player_name, college, college_state]
    if current_line_list[8] not in escuela_dict.keys():
      escuela_dict[current_line_list[8]] = [single_player_list]
    else:
      escuela_dict[current_line_list[8]].append(single_player_list)
      
if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("Map Blue", 113, 65, 5, 4)
  defineColor("Map Gray", 0, 0, 0, 44)
  
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
  
  left_margin = createImage(0, 36, 36, 720)
  loadImage("./border_pattern.jpg", left_margin); setScaleImageToFrame(1, 1, left_margin)
  right_margin = createImage(576, 36, 36, 720)
  loadImage("./border_pattern.jpg", right_margin); setScaleImageToFrame(1, 1, right_margin)
  
  page_header = createText(36, 9, 540, 36)
  setText("Where they are from - High School", page_header)
  setTextColor("White", page_header)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
  setTextAlignment(ALIGN_CENTERED, page_header)
    
  years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
  years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
  setTextColor("White", years1); setTextColor("White", years2)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
  setLineSpacing(7, years1); setLineSpacing(7, years2)
  
  thumb_w = 24.73
  thumb_h = 34
  
  page_num_rows = 18
  page_num_escuela = 0
  escuela_h = 44; escuela_x = 36 + 4
  y_offset = 0
  escuelas = list(escuela_dict.keys())
  escuelas = sorted(escuelas)
  for escuela in escuelas:
    num_players = len(escuela_dict[escuela])
    if (num_players % 2) == 0: num_rows = num_players / 2
    else: num_rows = (num_players / 2) + 1
    if ((720 - y_offset) < (36 *(num_rows + 2)) ):
      newPage(-1)
      top_rect = createRect(0, 0, 612, 36)
      setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
      bottom_rect = createRect(0, 756, 612, 36)
      setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
      center_rect = createRect(0, 36, 612, 720)
      setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
      left_margin = createImage(0, 36, 36, 720)
      loadImage("./border_pattern.jpg", left_margin); setScaleImageToFrame(1, 1, left_margin)
      right_margin = createImage(576, 36, 36, 720)
      loadImage("./border_pattern.jpg", right_margin); setScaleImageToFrame(1, 1, right_margin)
      
      page_header = createText(36, 9, 540, 36)
      setText("Where they are from - High School", page_header)
      setTextColor("White", page_header)
      setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
      setTextAlignment(ALIGN_CENTERED, page_header)
      
      years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
      years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
      setTextColor("White", years1); setTextColor("White", years2)
      setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
      setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
      setLineSpacing(7, years1); setLineSpacing(7, years2)
      page_num_rows = 18
      y_offset = 0
    
    escuela_banner_pos = 36 + 18 + y_offset
    escuela_banner = createRect(36, escuela_banner_pos, 540, 54)
    setFillColor("White", escuela_banner); setLineColor("NJCAA Blue", escuela_banner)
    escuela_y = escuela_banner_pos + (54.0 - escuela_h) / 2.0
    escuela_w = escuela_h / escuelas_dict[escuela.replace(" ", "_")]
    escuela_logo = createImage(escuela_x, escuela_y, escuela_w, escuela_h)
    loadImage("./Escuelas/"+ escuela.replace(" ", "_") + ".png", escuela_logo); setScaleImageToFrame(1, 1, escuela_logo)
    
    escuela_name = createText(escuela_x + escuela_w + 8, escuela_banner_pos + (54.0 - 24.0) / 2.0 + 3.0, 485, 28)
    setText(escuela + " - " + escuelas_cities_dict[escuela], escuela_name)
    setFont("Playball Regular", escuela_name); setFontSize(22, escuela_name); setTextColor("NJCAA Blue", escuela_name)
    
    player_count = 0
    players_list_size = len(escuela_dict[escuela])
    for col in range(2):
      thumb_name_w = 60
      thumb_college_w = 110
      thumb_state_w = 67
      thumb_name_frame = createText(270 * col + 36 + 4 + thumb_w + 4, escuela_banner_pos + 54 + 8, thumb_name_w, num_rows * 36)
      thumb_college_frame = createText(270 * col + 36 + 4 + thumb_w + 4 + thumb_name_w , escuela_banner_pos + 54 + 8, thumb_college_w, num_rows * 36)
      thumb_state_frame = createText(270 * col + 36 + 4 + thumb_w + 4 + thumb_name_w + thumb_college_w, escuela_banner_pos + 54 + 8 + 6, thumb_state_w, num_rows * 36)
      for row in range(num_rows):
        if ((row) % 2) == 0:
          blue_row = createRect((270 * col + 36), (y_offset + 108 + row * 36), 270, 36)
          setFillColor("Map Blue", blue_row); setLineColor("NJCAA Blue", blue_row)
        else:
          white_row = createRect((270 * col + 36), (y_offset +108 + row * 36), 270, 36)
          setFillColor("White", white_row); setLineColor("NJCAA Blue", white_row)
        
        current_player = escuela_dict[escuela][player_count]
        
        thumb_x = 270 * col + 36 + 4
        thumb_y = (y_offset + 108 + row * 36)
        player_thumb = createImage(thumb_x + 1,thumb_y + 1, thumb_w, thumb_h)
        loadImage(current_player[0], player_thumb); setScaleImageToFrame(1, 1, player_thumb)
        
        insertText(current_player[1].replace(" ", "\n", 1) + "\n\n", -1, thumb_name_frame)
        
        player_college_array = current_player[2].split(" ")
        if len(player_college_array) > 2: player_college = " ".join(player_college_array[0:2]) + "\n" + " ".join(player_college_array[2:])
        else: player_college = " ".join(player_college_array[0:1]) + "\n" + " ".join(player_college_array[1:])
        insertText(player_college + "\n\n", -1, thumb_college_frame)
        
        insertText(current_player[3] + "\n\n\n", -1, thumb_state_frame)
        player_count += 1
        if player_count == players_list_size: break
        # current_player = muni_dict[municip][player_count]
        # thumb_x = 270 * col + 36 + 4
        # thumb_y = 36 + row * 36
        # player_thumb = createImage(thumb_x,thumb_y, thumb_w, thumb_h)
        # loadImage(current_player[0], player_thumb); setScaleImageToFrame(1, 1, player_thumb)
    
      setFont("Asimov Print C", thumb_name_frame); setFontSize(8.5, thumb_name_frame)
      setTextColor("NJCAA Blue", thumb_name_frame); setLineSpacing(12, thumb_name_frame)
      setFont("Asimov Print C", thumb_college_frame); setFontSize(8.5, thumb_college_frame)
      setTextColor("NJCAA Blue", thumb_college_frame); setLineSpacing(12, thumb_college_frame)
      setFont("Asimov Print C", thumb_state_frame); setFontSize(8.5, thumb_state_frame)
      setTextColor("NJCAA Blue", thumb_state_frame); setLineSpacing(12, thumb_state_frame)
      selectObject(thumb_name_frame); moveSelectionToFront()
      selectObject(thumb_college_frame); moveSelectionToFront()
      selectObject(thumb_state_frame); moveSelectionToFront()
      selectObject(player_thumb); moveSelectionToFront()
      if player_count == players_list_size: break
    
    y_offset += 36 * num_rows + 72
    page_num_rows -= (1 + num_rows)
    page_num_escuela += 1
    # if page_num_escuela == 13: exit()
    # if (2 * page_num_municip + page_num_rows) > 17:
      # newPage(-1)
      # page_num_rows = 0
      # page_num_municip = 0
  