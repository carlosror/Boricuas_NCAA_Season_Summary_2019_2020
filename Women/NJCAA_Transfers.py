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

school_logos_dict = {}
with open("./School_Logos/filesizes_gif.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    school_logos_dict[current_line_list[0]] = float(current_line_list[2]) / float (current_line_list[1])

conf_logos_dict = {}
with open("./Conference_Logos/filesizes_png.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    conf_logos_dict[current_line_list[0]] = float(current_line_list[2]) / float (current_line_list[1])
                     

players_list = []
players_names_list = []
with open("NJCAA_Transfers.csv") as f:
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
        image_filename = "./" + "NJCAA_Transfers/doc/"  + first_name + "_" + full_name[1] + "_" + full_name[2] + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./"  + "NJCAA_Transfers/doc/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
    else:
      player_name = first_name + " " + first_last_name
      if (player_name in players_names_list): 
        player_name_count = sum([1 for plyr in players_names_list if plyr == player_name])
        image_filename = "./" + "NJCAA_Transfers/doc/" + first_name + "_" + first_last_name + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./"  + "NJCAA_Transfers/doc/" + first_name + "_" + first_last_name + ".jpg"
      
    player_from_school = current_line_list[1]
    player_from_school_state = current_line_list[2]
    player_from_school_division = current_line_list[3]
    player_to_school = current_line_list[4]
    player_to_school_state = current_line_list[5]
    player_to_school_division = current_line_list[6]
    
    single_player_list = [player_name, image_filename, player_from_school, player_from_school_state, player_from_school_division, player_to_school, player_to_school_state, player_to_school_division]
    players_list.append(single_player_list)
    players_names_list.append(player_name)


if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
    
  num_players = len(players_list)
  if (num_players % 9) == 0: 
    num_pages = (num_players / 9) 
  else: 
    num_pages = (num_players / 9) + 1
  player_count = 0
  for page in range(num_pages):
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    center_rect = createRect(0, 36, 612, 720)
    setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    
    page_header = createText(36, 9, 540, 80)
    page_title = "NJCAA Transfers\n"
    # page_subtitle = "Players with 500+ digs"
    insertText(page_title, -1, page_header)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
    # title_length = getTextLength(page_header)
    # subtitle_length = len(page_subtitle) 
    # insertText(page_subtitle, -1, page_header)
    # selectText(title_length, subtitle_length, page_header)
    # setFont("Playball Regular", page_header); setFontSize(26, page_header)
    setLineSpacing(30, page_header); setTextColor("White", page_header); setTextAlignment(ALIGN_CENTERED, page_header)
    
    
    years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
    years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
    setTextColor("White", years1); setTextColor("White", years2)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
    setLineSpacing(7, years1); setLineSpacing(7, years2)
    
    for row in range(3):
      for col in range(3):
        current_player = players_list[player_count]
        x_pos_tile = 36 + col * (174 + 9)
        y_pos_tile = 36 + 3.75 + row * (235 + 3.75)
        tile_width = 174
        player_name_banner_height = 20
        player_name_banner = createRect(x_pos_tile, y_pos_tile, tile_width, player_name_banner_height)
        setFillColor("NJCAA Blue", player_name_banner); setLineColor("NJCAA Blue", player_name_banner)
        player_name_text = createText(x_pos_tile, y_pos_tile + 5, tile_width, player_name_banner_height)
        insertText(current_player[0], -1, player_name_text)
        setFont("News of the World Wide Italic", player_name_text); setFontSize(17, player_name_text)
        setTextColor("White", player_name_text); setTextAlignment(ALIGN_CENTERED, player_name_text)
                
        current_player = players_list[player_count]
        photo_x = 36 + col * (174 + 9)
        # photo_y = 36 + 20 + row * (250 + 100)
        photo_y = y_pos_tile + player_name_banner_height 
        photo_height = 140
        player_photo = createImage(photo_x, photo_y, tile_width, photo_height)
        loadImage(current_player[1], player_photo); setScaleImageToFrame(1, 1, player_photo)
        
        banner_x = photo_x
        banner_y = photo_y + photo_height
        player_from_banner_height = 37
        player_from_banner = createRect(banner_x, banner_y, 174, player_from_banner_height)
        setFillColor("Darker Gray", player_from_banner); setLineColor("Darker Gray", player_from_banner)
        player_to_banner_height = 37
        player_to_banner = createRect(banner_x, banner_y + player_from_banner_height, 174, player_from_banner_height)
        setFillColor("White", player_to_banner); setLineColor("White", player_to_banner)
        
        player_from_to_text_w = 30
        player_from_to_text = createText(banner_x + 4, banner_y + 14, player_from_to_text_w, 60)
        insertText("From\n\n\nTo", -1, player_from_to_text)
        setFont("News of the World Wide Italic", player_from_to_text); setFontSize(12, player_from_to_text)
        setTextColor("NJCAA Blue", player_from_to_text); setTextAlignment(ALIGN_LEFT, player_from_to_text)
        setLineSpacing(13, player_from_to_text)
        
        # academic_logo = createImage(banner_x + 2, banner_y + 2, 40, 40)
        # loadImage("./All_Academic/All_Academic_logo.png", academic_logo); setScaleImageToFrame(1, 1, academic_logo)
        
        player_from_logo_name = current_player[2].replace(" ", "_")
        logo_width = 25.0
        from_logo_height = min(logo_width * school_logos_dict[player_from_logo_name], 35)
        from_logo_xpos = banner_x + 4 + player_from_to_text_w
        from_logo_ypos = banner_y + ((player_from_banner_height - from_logo_height) / 2.0)
        school_from_logo = createImage(from_logo_xpos, from_logo_ypos, logo_width, from_logo_height)
        loadImage("./School_Logos/" + player_from_logo_name + ".gif", school_from_logo); setScaleImageToFrame(1, 1, school_from_logo)
        
        school_from_name_xpos = from_logo_xpos + 25
        offset = 2
        school_from_name = createText(school_from_name_xpos, banner_y + offset, 90, player_from_banner_height)
        insertText(current_player[2] + "\n", -1, school_from_name)
        setFont("Asimov Print C", school_from_name); setFontSize(7, school_from_name)
        name_length = getTextLength(school_from_name)
        player_school_state = current_player[3]
        school_state_length = len(player_school_state) + 1
        insertText(player_school_state + "\n", -1, school_from_name)
        selectText(name_length, school_state_length, school_from_name)
        setFont("Playball Regular", school_from_name)
        player_school_division = current_player[4]
        player_school_division_length = len(player_school_division) + 1
        insertText(player_school_division + "\n", -1, school_from_name)
        selectText(name_length + school_state_length, player_school_division_length, school_from_name)
        setFont("Asimov Print C", school_from_name)
        setTextColor("NJCAA Blue", school_from_name)
        setLineSpacing(9, school_from_name)
        setTextAlignment(ALIGN_CENTERED, school_from_name)
        
        player_from_logo_division = current_player[4].replace(" ", "_")
        from_logo_xpos_div = banner_x + 4 + player_from_to_text_w + logo_width + 90
        from_logo_ypos_div = banner_y + 14 - 7
        from_logo_div_height = 25
        school_to_logo = createImage(from_logo_xpos_div, from_logo_ypos_div, logo_width, from_logo_div_height)
        loadImage("./Division_logos/" + player_from_logo_division + "_logo.png", school_to_logo); setScaleImageToFrame(1, 1, school_to_logo)
        
        player_to_logo_name = current_player[5].replace(" ", "_")
        logo_width = 25.0
        to_logo_height = min(logo_width * school_logos_dict[player_to_logo_name], 35)
        to_logo_xpos = banner_x + 4 + player_from_to_text_w
        to_logo_ypos = banner_y + player_from_banner_height + ((player_from_banner_height - to_logo_height) / 2.0)
        school_to_logo = createImage(to_logo_xpos, to_logo_ypos, logo_width, to_logo_height)
        loadImage("./School_Logos/" + player_to_logo_name + ".gif", school_to_logo); setScaleImageToFrame(1, 1, school_to_logo)
        
        school_to_name_xpos = to_logo_xpos + 25
        offset = 2
        school_to_name = createText(school_to_name_xpos, banner_y + player_from_banner_height + offset, 90, player_from_banner_height)
        insertText(current_player[5] + "\n", -1, school_to_name)
        setFont("Asimov Print C", school_to_name); setFontSize(7, school_to_name)
        name_length = getTextLength(school_to_name)
        player_school_state = current_player[6]
        school_state_length = len(player_school_state) + 1
        insertText(player_school_state + "\n", -1, school_to_name)
        selectText(name_length, school_state_length, school_to_name)
        setFont("Playball Regular", school_to_name)
        player_school_division = current_player[7].replace("\n", "")
        player_school_division_length = len(player_school_division) + 1
        insertText(player_school_division + "\n", -1, school_to_name)
        selectText(name_length + school_state_length, player_school_division_length, school_to_name)
        setFont("Asimov Print C", school_to_name)
        setTextColor("NJCAA Blue", school_to_name)
        setLineSpacing(9, school_to_name)
        setTextAlignment(ALIGN_CENTERED, school_to_name)
        
        division_x = photo_x + 5
        if (current_player[7].replace("\n","") in ["NCAA DI", "NCAA DII", "NCAA DIII", "NJCAA DI", "NJCAA DII"]):
          to_logo_ypos_div = from_logo_ypos_div + 37
          player_division = createImage(school_from_name_xpos + 90, to_logo_ypos_div, logo_width, from_logo_div_height)
        else:
          to_logo_ypos_div = from_logo_ypos_div + 37 + 7
          player_division = createImage(school_from_name_xpos + 90, to_logo_ypos_div, logo_width, 12)
        loadImage("./Division_logos/" + current_player[7].replace(" ", "_").replace("\n","") + "_logo.png", player_division); setScaleImageToFrame(1, 1, player_division)
                
              
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
  