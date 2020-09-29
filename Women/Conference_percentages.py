#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

# Dictionary of logos' height/width aspect ratios. It is used to position the school logo
# There's no way to programatically adjust frame to image.
# The Python Scribus uses doesn't have any image utilities like PIL so I could not
# figure out a way to determine the image's aspect ratio programatically. :|
# There is a program I wrote called Logo_aspect_ratio.py that takes all the images files
# in a directory and generates a CSV file of their width and height. The program is located in 
# the Women directory. After you run that program, you can run this one.

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  # Define colors and create headers
  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
  defineColor("NAIA Red", 8, 237, 198, 18)
  defineColor("NCAA Blue", 230, 163, 0, 0)
    
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    
  page_header = createText(36, 9, 540, 36)
  setText("Where they play - divisions & teams", page_header)
  setTextColor("White", page_header)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(26, page_header)
  setTextAlignment(ALIGN_CENTERED, page_header)
  
  years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
  years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
  setTextColor("White", years1); setTextColor("White", years2)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
  setLineSpacing(7, years1); setLineSpacing(7, years2)
  
  # Insert barplot
  barplot_x = 36; barplot_y = 50; barplot_w = 540; barplot_h = 290
  barplot = createImage(barplot_x, barplot_y, barplot_w, barplot_h)
  loadImage("conference_pctgs_chart.png", barplot); setScaleImageToFrame(1, 1, barplot)
  
  # Small banner towards the middle
  small_banner_y = barplot_y + 306
  small_banner_h = 24
  small_banner = createRect(barplot_x, small_banner_y, barplot_w, small_banner_h)
  setFillColor("NJCAA Blue", small_banner); setLineColor("NJCAA Blue", small_banner)
  small_banner_text = createText(barplot_x, small_banner_y + 3, barplot_w, small_banner_h)
  setText("Teams with the most players from Puerto Rico by division", small_banner_text); setTextColor("White", small_banner_text)
  setFont("Playball Regular", small_banner_text); setFontSize(20, small_banner_text); setTextAlignment(ALIGN_CENTERED, small_banner_text)
  
  conf_dict = {0: "NAIA", 1: "NCAA_DI", 2: "NCAA_DII", 3: "NCAA_DIII", 4: "NJCAA_DI", 5: "NJCAA_DII"}
  for conf in conf_dict.keys():
    table_w = 175
    if conf > 2: 
      table_x = 36 + (conf - 3) * (table_w + 7.5)
      table_y = (small_banner_y + 40) + 180 
    else: 
      table_x = 36 + conf * (table_w + 7.5)
      table_y = (small_banner_y + 40)
    table_header_height = 20
    table_header = createRect(table_x, table_y, table_w, table_header_height)
    if conf_dict[conf] in ["NCAA_DI", "NCAA_DII", "NCAA_DIII"]: setFillColor("NCAA Blue", table_header); setLineColor("NCAA Blue", table_header)
    elif conf_dict[conf] == "NAIA": setFillColor("NAIA Red", table_header); setLineColor("NAIA Red", table_header)
    else: setFillColor("NJCAA Blue", table_header); setLineColor("NJCAA Blue", table_header)
    table_header_text = createText(table_x, table_y + 3, table_w, table_header_height)
    setText(conf_dict[conf].replace("_", " "), table_header_text); setTextColor("White", table_header_text)
    setFont("Asimov Print C", table_header_text); setFontSize(17, table_header_text); setTextAlignment(ALIGN_CENTERED, table_header_text)
    
    num_rows = 10
    row_h = 14
    for row in range(num_rows):
      this_row = createRect(table_x, (table_y + table_header_height + row * row_h), table_w, row_h)
      if ((row + 1) % 2) == 0:
        setFillColor("Darker Gray", this_row); setLineColor("Darker Gray", this_row)
      else:
        setFillColor("White", this_row); setLineColor("White", this_row)
        
    team_counts_frame_schools = createText(table_x, table_y + table_header_height + 3, 0.9 * table_w, 10 * row_h + 4)
    team_counts_frame_num = createText(table_x + 0.9 * table_w, table_y + table_header_height + 3, 0.1 * table_w, 10 * row_h + 4)
    with open("team_counts_" + conf_dict[conf] + ".csv") as f2:
      next(f2)
      for line in f2:
        current_line_list = line.split(",")
        insertText(current_line_list[0] + "\n", -1, team_counts_frame_schools)
        insertText(current_line_list[1] + "\n", -1, team_counts_frame_num)
        
    setFont("Asimov Print C", team_counts_frame_schools); setFontSize(8.5, team_counts_frame_schools)
    setTextColor("NJCAA Blue", team_counts_frame_schools); setLineSpacing(14, team_counts_frame_schools)
    setFont("Asimov Print C", team_counts_frame_num); setFontSize(8.5, team_counts_frame_num)
    setTextColor("NJCAA Blue", team_counts_frame_num); setLineSpacing(7, team_counts_frame_num); setTextAlignment(ALIGN_CENTERED, team_counts_frame_num)