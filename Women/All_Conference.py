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
with open("All_Conference.csv") as f:
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
        image_filename = "./" + "All_Conference/"  + first_name + "_" + full_name[1] + "_" + full_name[2] + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./"  + "All_Conference/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
    else:
      player_name = first_name + " " + first_last_name
      if (player_name in players_names_list): 
        player_name_count = sum([1 for plyr in players_names_list if plyr == player_name])
        image_filename = "./" + "All_Conference/" + first_name + "_" + first_last_name + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./"  + "All_Conference/" + first_name + "_" + first_last_name + ".jpg"
      
    player_school = current_line_list[1]
    school_state = current_line_list[2]
    if current_line_list[2] == "Washington D.C.": school_state = "Washington, D.C."
    player_conf = current_line_list[3]
    school_division = current_line_list[4]
    player_award = current_line_list[5]
    photo_credit = current_line_list[7]
    
    single_player_list = [player_name, image_filename, player_school, school_state, player_conf, school_division, player_award, photo_credit]
    players_list.append(single_player_list)
    players_names_list.append(player_name)


if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
    
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
    
    page_header = createText(36, 9, 540, 36)
    setText("All-Conference Players", page_header)
    setTextColor("White", page_header)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
    setTextAlignment(ALIGN_CENTERED, page_header)
    
    years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
    years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
    setTextColor("White", years1); setTextColor("White", years2)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
    setLineSpacing(7, years1); setLineSpacing(7, years2)
    if page == 0:
      header_asterisk = createText(465, 9, 12, 36)
      setText("*", header_asterisk); setTextColor("White", header_asterisk); setFontSize(18, header_asterisk)
      
      footer_asterisk = createText(36, 758, 5, 34)
      setText("*", footer_asterisk); setTextColor("White", footer_asterisk); setFontSize(10, footer_asterisk)
      
      footnote_frame = createText(40, 758, 536, 35)
      footnote = "Some of the NJCAA awards are called All-Region or All-District, instead of All-Conference. For some of the NJCAA conferences, " \
                 "like regions 2 and 24 I could not find the announcement." 
      setText(footnote, footnote_frame); setTextColor("White", footnote_frame); setFontSize(10, footnote_frame); setLineSpacing(11, footnote_frame)    
    
    for row in range(2):
      for col in range(3):
        current_player = players_list[player_count]
        x_pos_tile = 36 + col * (170 + 15)
        y_pos_tile = 36 + 10 + row * (345 + 10)
        tile_width = 170
        all_conf_banner_height = 24
        all_conf_banner = createRect(x_pos_tile, y_pos_tile, tile_width, all_conf_banner_height)
        setFillColor("NJCAA Blue", all_conf_banner); setLineColor("NJCAA Blue", all_conf_banner)
        all_conf_text = createText(x_pos_tile, y_pos_tile + 6.5, tile_width, all_conf_banner_height)
        insertText("All-Conference", -1, all_conf_text)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", all_conf_text); setFontSize(13, all_conf_text)
        setTextColor("White", all_conf_text); setTextAlignment(ALIGN_CENTERED, all_conf_text)
        star_1 = createImage(x_pos_tile + 2, y_pos_tile + 2, 20, 20)
        loadImage("Star.png", star_1); setScaleImageToFrame(1, 1, star_1)
        star_2 = createImage(x_pos_tile + 149, y_pos_tile + 2, 20, 20)
        loadImage("Star.png", star_2); setScaleImageToFrame(1, 1, star_2)
                
        all_conf_banner_2_height = 15
        all_conf_banner_2 = createRect(x_pos_tile, y_pos_tile + all_conf_banner_height, tile_width, all_conf_banner_2_height)
        setFillColor("Darker Gray", all_conf_banner_2); setLineColor("Darker Gray", all_conf_banner_2)
        all_conf_text_2 = createText(x_pos_tile, y_pos_tile + all_conf_banner_height + 3, tile_width, all_conf_banner_2_height)
        insertText(current_player[6], -1, all_conf_text_2)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", all_conf_text_2); setFontSize(12, all_conf_text_2)
        setTextColor("NJCAA Blue", all_conf_text_2); setTextAlignment(ALIGN_CENTERED, all_conf_text_2)
        
        photo_x = x_pos_tile
        # photo_y = 36 + 20 + row * (250 + 100)
        photo_y = y_pos_tile + all_conf_banner_height + all_conf_banner_2_height
        player_photo = createImage(photo_x, photo_y, 170, 250)
        loadImage(current_player[1], player_photo); setScaleImageToFrame(1, 1, player_photo)
        
        photo_credit = "Photo: " + current_player[7].replace("\n", "")
        photo_credit_length = len(photo_credit)
        photo_credit_width = 3.0 * photo_credit_length + 2.5
        photo_credit_banner = createRect(photo_x + 170.0 - photo_credit_width, photo_y, photo_credit_width, 8)
        setFillColor("NJCAA Blue", photo_credit_banner); setLineColor("None", photo_credit_banner); setFillTransparency(0.70, photo_credit_banner)
        
        
        photo_credit_text = createText(photo_x + 170.0 - photo_credit_width, photo_y + 1.5, photo_credit_width, 10)
        setText(photo_credit, photo_credit_text)
        setTextColor("White", photo_credit_text); setFont("Asimov Print C", photo_credit_text); setFontSize(6, photo_credit_text)
        setTextAlignment(ALIGN_CENTERED, photo_credit_text)
        
        division_x = photo_x + 5
        if (current_player[5].replace("\n","") in ["NCAA DI", "NCAA DII", "NCAA DIII", "NJCAA DI", "NJCAA DII"]):
          division_y = photo_y + 5
          player_division = createImage(division_x, division_y, 25, 25)
        else:
          division_y = photo_y + 10
          player_division = createImage(division_x, division_y, 25, 12)
        loadImage("./Division_logos/" + current_player[5].replace(" ", "_").replace("\n","") + "_logo.png", player_division); setScaleImageToFrame(1, 1, player_division)
        
        
        banner_x = photo_x
        banner_y = photo_y + 250
        player_banner_height = 30
        player_banner = createRect(banner_x, banner_y, 170, player_banner_height)
        setFillColor("White", player_banner); setLineColor("None", player_banner)
        
        # academic_logo = createImage(banner_x + 2, banner_y + 2, 40, 40)
        # loadImage("./All_Academic/All_Academic_logo.png", academic_logo); setScaleImageToFrame(1, 1, academic_logo)
        
        logo_name = current_player[2].replace(" ", "_")
        if (school_logos_dict[logo_name] < 0.7):
          logo_width = 33.0
          logo_height = min(logo_width * school_logos_dict[logo_name], 28)
        else:
          logo_height = 28.0
          logo_width = min(logo_height / school_logos_dict[logo_name], 33)
        logo_ypos = (banner_y + (player_banner_height - logo_height) / 2.0)
        school_logo = createImage(banner_x + 5, logo_ypos, logo_width, logo_height)
        loadImage("./School_Logos/" + logo_name + ".gif", school_logo); setScaleImageToFrame(1, 1, school_logo)
                
        
        vocales_acentos = ["Á", "É", "Í", "Ó", "Ú", "Ñ"]
        if any(x in unicode(current_player[0]).upper() for x in vocales_acentos): player_name_ypos = banner_y + 2
        else: player_name_ypos = banner_y + 4
        player_name = createText(banner_x + 33 + 5 + 1, player_name_ypos - 1, 132, 30)
        insertText(unicode(current_player[0]).upper() + "\n", -1, player_name)
        setFont("Asimov Print C", player_name); setFontSize(9, player_name)
        name_length = getTextLength(player_name)
        player_school = current_player[2]
        school_length = len(player_school) + 1
        insertText(unicode(player_school).upper() + "\n", -1, player_name)
        selectText(name_length, school_length, player_name)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_name)
        selectText(name_length, len(player_school), player_name); setFontSize(6.2, player_name)
        school_state = current_player[3]
        insertText(school_state, -1, player_name)
        selectText(name_length + school_length, len(school_state), player_name)
        setFont("Playball Regular", player_name)
        selectText(name_length + school_length, len(school_state), player_name); setFontSize(9, player_name)
        setTextColor("NJCAA Blue", player_name)
        setLineSpacing(9, player_name)
        setTextAlignment(ALIGN_CENTERED, player_name)
                
        
        player_conf_background_height = 24.0
        player_conf_background = createRect(banner_x + 0.5, banner_y + player_banner_height, 170, player_conf_background_height)
        setFillColor("Darker Gray", player_conf_background); setLineColor("Darker Gray", player_conf_background)
        
        player_conf_img = current_player[4].replace(" ", "_")
        if (conf_logos_dict[player_conf_img] < 0.7): # C-USA and ASUN are very wide
          player_conf_logo_w = 33.0
          player_conf_logo_h = min(player_conf_logo_w * conf_logos_dict[player_conf_img], 22.0)
        else:
          player_conf_logo_h = 22.0
          player_conf_logo_w = min(player_conf_logo_h / conf_logos_dict[player_conf_img], 33.0)
        
        conf_logo = createImage(banner_x + 5, banner_y + player_banner_height + (player_conf_background_height - player_conf_logo_h) / 2.0, player_conf_logo_w, player_conf_logo_h)
        loadImage("./Conference_Logos/" + player_conf_img + ".png", conf_logo); setScaleImageToFrame(1, 1, conf_logo)
        
        offset = 9.0
        if len(current_player[4]) > 28: offset = 3.5
        player_conf_frame = createText(banner_x + 33 + 5 + 1, banner_y + player_banner_height + offset, 132, 23)
        # player_conf_array = current_player[4].split(" ")
        # player_conf_array_length = len(player_conf_array)
        # if (player_conf_array_length % 2) == 0: split_point = player_conf_array_length / 2
        # else: split_point = (player_conf_array_length / 2) + 1
        # player_conf = " ".join(player_conf_array[0:split_point]) + "\n" + " ".join(player_conf_array[split_point:])
        player_conf = current_player[4]
        # player_conf_length = len(player_conf)
        insertText(player_conf, -1, player_conf_frame)
        setTextColor("NJCAA Blue", player_conf_frame)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_conf_frame); setFontSize(8, player_conf_frame)
        setLineSpacing(11, player_conf_frame); setTextAlignment(ALIGN_CENTERED, player_conf_frame)
        
                        
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
  