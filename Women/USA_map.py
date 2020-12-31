#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
import time
margins = (36, 36, 0, 0)

states_list = []
with open("./player_counts_states.csv") as f:
  next(f)
  for line in f:
    current_line_list = line.split(",")
    state = current_line_list[0]
    flag_filename = "./../Women/State_flags/" + state.replace(" ", "_").replace(".", "") + ".png"
    if state == "Washington D.C.": state = "Washington, D.C."
    player_count = current_line_list[1]
    single_state_list = [flag_filename, state, player_count]
    states_list.append(single_state_list)

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
  
  page_header = createText(36, 9, 540, 36)
  setText("Where they play - States", page_header)
  setTextColor("White", page_header)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
  setTextAlignment(ALIGN_CENTERED, page_header)
    
  years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
  years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
  setTextColor("White", years1); setTextColor("White", years2)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
  setLineSpacing(7, years1); setLineSpacing(7, years2)
  
  map_height = 252
  usa_map = createImage(36, 54, 540, map_height)
  loadImage("./../Maps/usa_map10.png", usa_map); setScaleImageToFrame(1, 1, usa_map)
  setLineColor("NJCAA Blue", usa_map)
  
  states_list_size = len(states_list)
  if (states_list_size % 3) == 0: num_rows = states_list_size / 3
  else: num_rows = (states_list_size / 3) + 1
  
  offset = 36 + 18 + map_height + 36
  for row in range(num_rows):
    this_row = createRect(36, (offset + row * 32), 540, 32)
    if ((row + 1) % 2) == 0:
      setFillColor("Map Blue", this_row); setLineColor("Map Blue", this_row)
    else:
      setFillColor("White", this_row); setLineColor("White", this_row)
      
  flag_w = 45
  flag_h = 30
  state_count = 0
  for col in range(3):
    flag_name_w = 95
    num_players_w = 15
    
    flag_name_frame = createText(180 * col + 36 + 5 + flag_w + 5, offset + 11, flag_name_w, 32 * num_rows)
    # setFont("Asimov Print C", flag_name_frame); setFontSize(12, flag_name_frame)
    # setTextColor("NJCAA Blue", flag_name_frame); setLineSpacing(10.65, flag_name_frame)
    
    num_players_frame = createText(180 * col + 36 + 5 + flag_w + 5 + flag_name_w, offset + 11, num_players_w, 32 * num_rows)
    # setFont("Asimov Print C", num_players_frame); setFontSize(12, num_players_frame)
    # setTextColor("NJCAA Blue", num_players_frame); setLineSpacing(8.0, num_players_frame)
    # setTextAlignment(ALIGN_RIGHT, num_players_frame)
    for row in range(num_rows):
      
      current_state = states_list[state_count]
      
      flag_x = 180 * col + 36 + 5
      flag_y = offset + row * 32 + 0.5
      if (current_state[1] in ["Kentucky", "New York", "West Virginia", "Washington, D.C."]): flag_y += 3.5
      if (current_state[1] in ["Georgia", "Kansas", "Illinois", "Louisiana", "Massachusetts", "Nebrasks", "New Jersey", "Ohio", "Tennessee"]): flag_y += 1.0
      if (current_state[1] in ["Connecticut", "Maine"]): flag_x += 3.0
      flag = createImage(flag_x,flag_y, flag_w, flag_h)
      loadImage(current_state[0], flag); setScaleImageToFrame(1, 1, flag)
      
      insertText(current_state[1] + "\n\n\n", -1, flag_name_frame)
      insertText(current_state[2] + "\n\n\n", -1, num_players_frame)
      
      state_count += 1
      if state_count == states_list_size: break
    setFont("Asimov Print C", flag_name_frame); setFontSize(12, flag_name_frame)
    setTextColor("NJCAA Blue", flag_name_frame); setLineSpacing(10.65, flag_name_frame)
    setFont("Asimov Print C", num_players_frame); setFontSize(12, num_players_frame)
    setTextColor("NJCAA Blue", num_players_frame); setLineSpacing(8.0, num_players_frame)
    setTextAlignment(ALIGN_RIGHT, num_players_frame)
    if state_count == states_list_size: break
    
      
  # setFont("Asimov Print C", flag_name_frame); setFontSize(12, flag_name_frame)
  