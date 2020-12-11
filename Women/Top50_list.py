#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

def draw_line(x1, y1, x2, y2, line_type = LINE_DASH, width = 1, color = "Map Blue"):
  this_line = createLine(x1, y1, x2, y2); setLineStyle(line_type, this_line); setLineColor(color, this_line)
  setLineWidth(width, this_line)

players_list = []
with open("Top50.csv") as f:
  next(f) # skip headers row
  for line in f:
    current_line_list = line.split(",")
    full_name = current_line_list[0].split()
    first_name = full_name[0]
    first_last_name = full_name[1]
    if (full_name[1] == "de" or full_name[1] == "La"):
      player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
    else:
      player_name = first_name + " " + first_last_name
      
    player_stat = current_line_list[1] + " " + current_line_list[2]
    player_rank = current_line_list[3]
    player_school = current_line_list[4]
    school_state = current_line_list[5]
    school_division = current_line_list[6]
    photo_credit = current_line_list[7]
    
    hometown = current_line_list[6]
    single_player_list = [player_name, player_school, school_state, school_division, player_stat, player_rank]
    players_list.append(single_player_list)
    
if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Map Blue", 113, 65, 5, 4)
  defineColor("Map Gray", 0, 0, 0, 44)
  
  num_players = len(players_list)
  num_rows = 39
  if (num_players % num_rows) == 0: 
    num_pages = (num_players / num_rows) 
  else: 
    num_pages = (num_players / num_rows) + 1
  
  header_height = 18
  offset = 36 + 0 + header_height
  row_height = 18
  total_num_rows = 0
  player_count = 0
  for page in range(num_pages):
    
    left_margin = createImage(0, 36, 36, 720)
    loadImage("./border_pattern.jpg", left_margin); setScaleImageToFrame(1, 1, left_margin)
    
    right_margin = createImage(576, 36, 36, 720)
    loadImage("./border_pattern.jpg", right_margin); setScaleImageToFrame(1, 1, right_margin)
    
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    
    page_header = createText(36, 9, 540, 36)
    setText("Top 50 List", page_header)
    setTextColor("White", page_header)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
    setTextAlignment(ALIGN_CENTERED, page_header)
    
    years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
    years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
    setTextColor("White", years1); setTextColor("White", years2)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
    setLineSpacing(7, years1); setLineSpacing(7, years2) 
    
    for row in range(num_rows):
      this_row = createRect(36, (offset + row * row_height), 540, row_height)
      if ((row + 1) % 2) == 0:
        setFillColor("Map Blue", this_row); setLineColor("Map Blue", this_row)
      else:
        setFillColor("White", this_row); setLineColor("White", this_row)
      total_num_rows += 1
      if total_num_rows == num_players: 
        bottom_line_pos = (offset + row * row_height) + row_height
        break
          
    header = createRect(36, offset - header_height, 540, header_height)
    setFillColor("Map Gray", header); setLineColor("None", header)
    
    player_name_frame_width = 90; player_name_frame_xpos = 36 + 4
    player_name_frame = createText(player_name_frame_xpos, offset + 5, player_name_frame_width, num_rows * row_height)
    player_school_frame_width = 160; player_school_frame_xpos = player_name_frame_xpos + player_name_frame_width
    player_school_frame = createText(player_school_frame_xpos, offset + 5, player_school_frame_width, num_rows * row_height)
    player_school_state_frame_width = 70; player_school_state_frame_xpos = player_school_frame_width + player_school_frame_xpos
    player_school_state_frame = createText(player_school_state_frame_xpos, offset + 5, player_school_state_frame_width, num_rows * row_height)
    player_division_frame_width = 80; player_division_frame_xpos = player_school_state_frame_width + player_school_state_frame_xpos
    player_division_frame = createText(player_division_frame_xpos, offset + 5, player_division_frame_width, num_rows * row_height)
    player_stat_frame_width = 80; player_stat_frame_xpos = player_division_frame_width + player_division_frame_xpos
    player_stat_frame = createText(player_stat_frame_xpos, offset + 5, player_stat_frame_width, num_rows * row_height)
    player_rank_frame_width = 50; player_rank_frame_xpos = player_stat_frame_width + player_stat_frame_xpos
    player_rank_frame = createText(player_rank_frame_xpos, offset + 5, player_rank_frame_width, num_rows * row_height)
    
    # Headers
    player_name_frame_header = createText(player_name_frame_xpos, offset - header_height + 4, player_name_frame_width, header_height)
    insertText("Player", -1, player_name_frame_header)
    setFont("Asimov Print C", player_name_frame_header); setFontSize(12, player_name_frame_header)
    setTextColor("NJCAA Blue", player_name_frame_header);
    player_school_frame_header = createText(player_school_frame_xpos, offset - header_height + 4, player_school_frame_width, header_height)
    insertText("School", -1, player_school_frame_header)
    setFont("Asimov Print C", player_school_frame_header); setFontSize(12, player_school_frame_header)
    setTextAlignment(ALIGN_CENTERED, player_school_frame_header); setTextColor("NJCAA Blue", player_school_frame_header);
    player_school_state_frame_header = createText(player_school_state_frame_xpos, offset - header_height + 4, player_school_state_frame_width, header_height)
    insertText("State", -1, player_school_state_frame_header)
    setFont("Asimov Print C", player_school_state_frame_header); setFontSize(12, player_school_state_frame_header)
    setTextAlignment(ALIGN_CENTERED, player_school_state_frame_header); setTextColor("NJCAA Blue", player_school_state_frame_header);
    player_division_frame_header = createText(player_division_frame_xpos, offset - header_height + 4, player_division_frame_width, header_height)
    insertText("Division", -1, player_division_frame_header)
    setFont("Asimov Print C", player_division_frame_header); setFontSize(12, player_division_frame_header)
    setTextAlignment(ALIGN_CENTERED, player_division_frame_header); setTextColor("NJCAA Blue", player_division_frame_header);
    player_stat_frame_header = createText(player_stat_frame_xpos, offset - header_height + 4, player_stat_frame_width, header_height)
    insertText("Statistic", -1, player_stat_frame_header)
    setFont("Asimov Print C", player_stat_frame_header); setFontSize(12, player_stat_frame_header)
    setTextAlignment(ALIGN_CENTERED, player_stat_frame_header); setTextColor("NJCAA Blue", player_stat_frame_header);
    player_rank_frame_header = createText(player_rank_frame_xpos, offset - header_height + 4, player_rank_frame_width, header_height)
    insertText("Rank", -1, player_rank_frame_header)
    setFont("Asimov Print C", player_rank_frame_header); setFontSize(12, player_rank_frame_header)
    setTextAlignment(ALIGN_CENTERED, player_rank_frame_header); setTextColor("NJCAA Blue", player_rank_frame_header);
      
    for row in range(num_rows):
      current_player = players_list[player_count]
      insertText(current_player[0] + 2 *"\n", -1, player_name_frame)
      insertText(current_player[1] + 2 *"\n", -1, player_school_frame)
      insertText(current_player[2] + 2 *"\n", -1, player_school_state_frame)
      insertText(current_player[3] + 2 *"\n", -1, player_division_frame)
      insertText(current_player[4] + 2 *"\n", -1, player_stat_frame)
      insertText(current_player[5] + 2 *"\n", -1, player_rank_frame)
      player_count += 1
      if player_count == num_players: break
    
    setFont("Asimov Print C", player_name_frame); setFontSize(8.5, player_name_frame); #setTextAlignment(ALIGN_CENTERED, player_name_frame)
    setTextColor("NJCAA Blue", player_name_frame); setLineSpacing(9.005, player_name_frame)
    setFont("Asimov Print C", player_school_frame); setFontSize(8.5, player_school_frame); setTextAlignment(ALIGN_CENTERED, player_school_frame)
    setTextColor("NJCAA Blue", player_school_frame); setLineSpacing(9.005, player_school_frame)
    setFont("Asimov Print C", player_school_state_frame); setFontSize(8.5, player_school_state_frame); setTextAlignment(ALIGN_CENTERED, player_school_state_frame)
    setTextColor("NJCAA Blue", player_school_state_frame); setLineSpacing(9.005, player_school_state_frame)
    setFont("Asimov Print C", player_division_frame); setFontSize(8.5, player_division_frame); setTextAlignment(ALIGN_CENTERED, player_division_frame)
    setTextColor("NJCAA Blue", player_division_frame); setLineSpacing(9.005, player_division_frame)
    setFont("Asimov Print C", player_stat_frame); setFontSize(8.5, player_stat_frame); setTextAlignment(ALIGN_CENTERED, player_stat_frame)
    setTextColor("NJCAA Blue", player_stat_frame); setLineSpacing(9.005, player_stat_frame)
    setFont("Asimov Print C", player_rank_frame); setFontSize(8.5, player_rank_frame); setTextAlignment(ALIGN_CENTERED, player_rank_frame)
    setTextColor("NJCAA Blue", player_rank_frame); setLineSpacing(9.005, player_rank_frame)
    
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    if player_count == num_players: 
      draw_line(36, bottom_line_pos, 576, bottom_line_pos, line_type = LINE_SOLID, color = "NJCAA Blue")
      for xpos in [36, player_school_frame_xpos, player_school_state_frame_xpos, player_division_frame_xpos, player_stat_frame_xpos, player_rank_frame_xpos, 576]:
        draw_line(xpos, bottom_line_pos, xpos, 36, line_type = LINE_SOLID, color = "NJCAA Blue")
      break
    else:
      for xpos in [36, player_school_frame_xpos, player_school_state_frame_xpos, player_division_frame_xpos, player_stat_frame_xpos, player_rank_frame_xpos, 576]:
        draw_line(xpos, 36, xpos, 756, line_type = LINE_SOLID, color = "NJCAA Blue")
    newPage(-1)