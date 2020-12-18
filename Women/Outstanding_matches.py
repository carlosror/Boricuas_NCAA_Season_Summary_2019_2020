#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

def text_frame(pos_x, pos_y, frame_width, frame_height, texts_list, fonts_list, font_sizes, colors, alignment = ALIGN_CENTERED, line_spacing = 24, scaling_h = 100):
  this_text_frame = createText(pos_x, pos_y, frame_width, frame_height)
  insertText(texts_list[0] + "\n", -1, this_text_frame)
  setFont(fonts_list[0], this_text_frame); setFontSize(font_sizes[0], this_text_frame); setTextColor(colors[0], this_text_frame)
  previous_line_length = getTextLength(this_text_frame)
  for idx in range(1,len(texts_list)):
    text_line = texts_list[idx]
    length_text_line = len(unicode(text_line))
    if idx < len(texts_list) - 1: insertText(text_line + "\n", -1, this_text_frame)
    else: insertText(text_line, -1, this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setFont(fonts_list[idx], this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setFontSize(font_sizes[idx], this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setTextColor(colors[idx], this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setTextAlignment(alignment, this_text_frame)
    previous_line_length += length_text_line + 1
  setTextAlignment(alignment, this_text_frame); setLineSpacing(line_spacing, this_text_frame)
  setTextScalingH(scaling_h, this_text_frame)

def draw_line(x1, y1, x2, y2, line_type = LINE_DASH, width = 1, color = "Map Blue"):
  this_line = createLine(x1, y1, x2, y2); setLineStyle(line_type, this_line); setLineColor(color, this_line)
  setLineWidth(width, this_line)
  
# Dictionary of logos' height/width aspect ratios. It is used to position the school logo
# There's no way to programatically adjust frame to image.
# The Python Scribus uses doesn't have any image utilities like PIL so I could not
# figure out a way to determine the image's aspect ratio programatically. :|
# There is a program I wrote called Logo_aspect_ratio.py that takes all the images files
# in a directory and generates a CSV file of their width and height. The program is located in 
# the Women directory. After you run that program, you can run this one.

school_logos_dict = {}
with open("./School_Logos/filesizes_gif.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    school_logos_dict[current_line_list[0]] = float(current_line_list[2]) / float (current_line_list[1])

tourney_logos_dict = {}
with open("./Tournament_Logos/filesizes_png.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    tourney_logos_dict[current_line_list[0]] = float(current_line_list[2]) / float (current_line_list[1])
                     
players_list = []
players_names_list = []
with open("Outstanding_matches.csv") as f:
  next(f) # skip headers row
  for line in f:
    current_line_list = line.split(",")
    full_name = current_line_list[0].split()
    first_name = full_name[0]
    first_last_name = full_name[1]
    if (full_name[1] == "de" or full_name[1] == "La"):
      player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
      if (player_name in players_names_list): 
        player_name_count = sum([1 for plyr in players_names_list if plyr == player_name])
        image_filename = "./Outstanding_matches/" + first_name + "_" + full_name[1] + "_" + full_name[2] + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./Outstanding_matches/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
    else:
      player_name = first_name + " " + first_last_name
      if (player_name in players_names_list): 
        player_name_count = sum([1 for plyr in players_names_list if plyr == player_name])
        image_filename = "./Outstanding_matches/" + first_name + "_" + first_last_name + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./Outstanding_matches/" + first_name + "_" + first_last_name + ".jpg"
      
    player_school = current_line_list[5] 
    school_state = current_line_list[6]
    division = current_line_list[7]
    player_stat1 = current_line_list[1]
    player_stat2 = current_line_list[2]
    photo_credit = current_line_list[8]
    date = current_line_list[3]
    
    single_player_list = [player_name, image_filename, player_stat1, player_stat2, player_school, school_state, division, photo_credit, date]
    players_list.append(single_player_list)
    players_names_list.append(player_name)


if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
  
  # top_right_rect = createRect(306, 36, 306, 180)
  # setFillColor("NJCAA Gray", top_right_rect); setLineColor("NJCAA Gray", top_right_rect)
  # second_rect = createRect(0, 216, 306, 180)
  # setFillColor("NJCAA Gray", second_rect); setLineColor("NJCAA Gray", second_rect)
  # third_rect = createRect(306, 396, 306, 180)
  # setFillColor("NJCAA Gray", third_rect); setLineColor("NJCAA Gray", third_rect)
  # top_left_rect = createRect(0, 576, 306, 180)
  # setFillColor("NJCAA Gray", top_left_rect); setLineColor("NJCAA Gray", top_left_rect)
  
  num_players = len(players_list)
  if (num_players % 6) == 0: 
    num_pages = (num_players / 6) 
  else: 
    num_pages = (num_players / 6) + 1
  player_count = 0
  for page in range(num_pages):
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    center_rect = createRect(0, 36, 612, 720)
    setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    
    page_header = createText(36, 9, 540, 80)
    page_title = "Outstanding Matches\n"
    insertText(page_title, -1, page_header)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
    setLineSpacing(30, page_header); setTextColor("White", page_header); setTextAlignment(ALIGN_CENTERED, page_header)
    
    
    years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
    years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
    setTextColor("White", years1); setTextColor("White", years2)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
    setLineSpacing(7, years1); setLineSpacing(7, years2)
    
    # left_margin = createImage(0, 36, 36, 720)
    # loadImage("./border_pattern.jpg", left_margin); setScaleImageToFrame(1, 1, left_margin)
    # right_margin = createImage(576, 36, 36, 720)
    # loadImage("./border_pattern.jpg", right_margin); setScaleImageToFrame(1, 1, right_margin)
    
    for row in range(2):
      for col in range(3):
        current_player = players_list[player_count]
        photo_x = 36 + col * (170 + 15)
        # photo_y = 36 + 20 + row * (250 + 100)
        photo_y = 36 + 30 + row * (250 + 95)
        player_photo = createImage(photo_x, photo_y, 170, 250)
        loadImage(current_player[1], player_photo); setScaleImageToFrame(1, 1, player_photo)
        
        photo_credit = "Photo: " + current_player[7].replace("\n", "")
        photo_credit_length = len(photo_credit)
        photo_credit_width = 3.0 * photo_credit_length + 5.5
        photo_credit_banner = createRect(photo_x + 170.0 - photo_credit_width, photo_y, photo_credit_width, 8)
        setFillColor("NJCAA Blue", photo_credit_banner); setLineColor("None", photo_credit_banner); setFillTransparency(0.70, photo_credit_banner)
        
        
        photo_credit_text = createText(photo_x + 170.0 - photo_credit_width, photo_y + 1.5, photo_credit_width, 10)
        setText(photo_credit, photo_credit_text)
        setTextColor("White", photo_credit_text); setFont("Asimov Print C", photo_credit_text); setFontSize(6, photo_credit_text)
        setTextAlignment(ALIGN_CENTERED, photo_credit_text)
        
        division_x = photo_x + 5
        if (current_player[6].replace("\n","") in ["NCAA DI", "NCAA DII", "NCAA DIII", "NJCAA DI", "NJCAA DII"]):
          division_y = photo_y + 5
          player_division = createImage(division_x, division_y, 25, 25)
        else:
          division_y = photo_y + 10
          player_division = createImage(division_x, division_y, 25, 12)
        loadImage("./Division_logos/" + current_player[6].replace(" ", "_").replace("\n","") + "_logo.png", player_division); setScaleImageToFrame(1, 1, player_division)
                
        banner_x = photo_x + 0.5; banner_height = 250 * 0.15 
        banner_y = photo_y + 250 - banner_height
        player_banner = createRect(banner_x, banner_y, 168.5, banner_height)
        setFillColor("White", player_banner); setLineColor("NJCAA Blue", player_banner)
        # setFillTransparency(0.70, player_banner)
        
        logo_name = current_player[4].replace(" ", "_")
        if (school_logos_dict[logo_name] < 0.7):
          logo_width = 33.0
          logo_height = min(logo_width * school_logos_dict[logo_name], 28)
        else:
          logo_height = 28.0
          logo_width = min(logo_height / school_logos_dict[logo_name], 33)
        logo_ypos = (banner_y + (banner_height - logo_height) / 2.0)
        school_logo = createImage(banner_x + 1, logo_ypos, logo_width, logo_height)
        loadImage("./School_Logos/" + logo_name + ".gif", school_logo); setScaleImageToFrame(1, 1, school_logo)
        
        # vocales_acentos = ["Á", "É", "Í", "Ó", "Ú", "Ñ"]
        # if any(x in unicode(current_player[0]).upper() for x in vocales_acentos): player_name_ypos = banner_y + 3
        # else: player_name_ypos = banner_y + 5
        # player_name = createText(banner_x + 2 + logo_width, player_name_ypos, 170 - 2 - logo_width, 250 * 0.15)
        # insertText(unicode(current_player[0]).upper() + "\n", -1, player_name)
        # setFont("Asimov Print C", player_name); setFontSize(9.4, player_name)
        # name_length = getTextLength(player_name)
        # player_school = current_player[4]
        # school_length = len(player_school) + 1
        # insertText(unicode(player_school).upper() + "\n", -1, player_name)
        # selectText(name_length, school_length, player_name)
        # setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_name)
        # selectText(name_length, len(player_school), player_name); setFontSize(5.5, player_name)
        # school_state = current_player[5]
        # insertText(school_state, -1, player_name)
        # selectText(name_length + school_length, len(school_state), player_name)
        # setFont("Playball Regular", player_name)
        # selectText(name_length + school_length, len(school_state), player_name); setFontSize(10, player_name)
        # setTextColor("NJCAA Blue", player_name)
        # setLineSpacing(11, player_name)
        # setTextAlignment(ALIGN_CENTERED, player_name)
        
        text_frame(banner_x + 2 + logo_width, banner_y + 4, 170 - 2 - logo_width, 250 * 0.15, [current_player[0], current_player[4], current_player[5]], 
        ["Asimov Print C", "OLD SPORT 02 ATHLETIC NCV Regular", "Playball Regular"], 
             [9.4, 5.5, 10], colors = ["NJCAA Blue" for idx in range(3)], line_spacing = 11)
        
        
        stat_banner_height = 45.0
        stat_banner = createRect(banner_x, photo_y + 250, 168.5, stat_banner_height)
        setFillColor("NJCAA Gray", stat_banner); setLineColor("NJCAA Blue", stat_banner)
        
        player_stat1 = current_player[2].split(" ")
        text_frame(photo_x, photo_y + 250 + 5, 85, 50, [player_stat1[0], player_stat1[1]], ["Pink Sans 130", "Arial Regular"], 
             [28, 12], colors = ["NJCAA Blue", "NJCAA Blue"], line_spacing = 15)
        player_stat2 = current_player[3].split(" ")
        text_frame(photo_x + 85, photo_y + 250 + 5, 85, 50, [player_stat2[0], player_stat2[1]], ["Pink Sans 130", "Arial Regular"], 
             [28, 12], colors = ["NJCAA Blue", "NJCAA Blue"], line_spacing = 15)

        draw_line(photo_x + 85, photo_y + 250, photo_x + 85, photo_y + 250 + stat_banner_height, line_type = LINE_SOLID, width = 0.5, color = "NJCAA Blue")
        
        date_banner_height = 20.0
        date_banner = createRect(banner_x, photo_y + 250 + stat_banner_height, 168.5, date_banner_height)
        setFillColor("NJCAA Blue", date_banner); setLineColor("Black", date_banner)
        text_frame(photo_x, photo_y + 250 + stat_banner_height + 5, 170, 22, [current_player[8]], ["Asimov Print C"], [12], ["White"])
        
        # date_text = createText(photo_x, photo_y + 250 + stat_banner_height + 5, 170, 22)
        # insertText(current_player[8], -1, date_text)
        # setTextColor("White", date_text); setFont("Asimov Print C", date_text)
        # setFontSize(12, date_text); setTextAlignment(ALIGN_CENTERED, date_text)
        
        player_count += 1
        if player_count == num_players: break
      if player_count == num_players: break
    if player_count == num_players: break
    # if page == 0: break
    
    
    # right_rect = createRect(576, 36, 36, 720)
    # setFillColor("NJCAA Gray", right_rect); setLineColor("NJCAA Gray", right_rect)
    # left_rect = createRect(0, 36, 36, 720)
    # setFillColor("NJCAA Gray", left_rect); setLineColor("NJCAA Gray", left_rect)
    newPage(-1)
  