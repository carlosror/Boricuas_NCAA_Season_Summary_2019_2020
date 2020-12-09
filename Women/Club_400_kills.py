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
with open("club_400_kills_photo.csv") as f:
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
        image_filename = "./" + "Club_400_kills/"  + first_name + "_" + full_name[1] + "_" + full_name[2] + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./"  + "Club_400_kills/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
    else:
      player_name = first_name + " " + first_last_name
      if (player_name in players_names_list): 
        player_name_count = sum([1 for plyr in players_names_list if plyr == player_name])
        image_filename = "./" + "Club_400_kills/" + first_name + "_" + first_last_name + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./"  + "Club_400_kills/" + first_name + "_" + first_last_name + ".jpg"
      
    player_school = current_line_list[1]
    school_state = current_line_list[2]
    if current_line_list[2] == "Washington D.C.": school_state = "Washington, D.C."
    player_conf = current_line_list[3]
    school_division = current_line_list[4]
    player_stat = current_line_list[8]
    player_photo = current_line_list[24]
    
    single_player_list = [player_name, image_filename, player_school, school_state, player_conf, school_division, player_stat, player_photo]
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
    top_rect = createRect(0, 0, 612, 72)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    center_rect = createRect(0, 72, 612, 684)
    setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    
    page_header = createText(36, 9, 540, 80)
    page_title = "The 400 Club\n"
    page_subtitle = "Players with 400+ kills"
    insertText(page_title, -1, page_header)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
    title_length = getTextLength(page_header)
    subtitle_length = len(page_subtitle) 
    insertText(page_subtitle, -1, page_header)
    selectText(title_length, subtitle_length, page_header)
    setFont("Playball Regular", page_header); setFontSize(26, page_header)
    setLineSpacing(30, page_header); setTextColor("White", page_header); setTextAlignment(ALIGN_CENTERED, page_header)
    
    
    years1 = createText(0, 24.5, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
    years2 = createText(576, 24.5, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
    setTextColor("White", years1); setTextColor("White", years2)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
    setLineSpacing(7, years1); setLineSpacing(7, years2)
    
    for row in range(3):
      for col in range(3):
        current_player = players_list[player_count]
        photo_x = 36 + col * (170 + 15)
        # photo_y = 36 + 20 + row * (250 + 100)
        photo_y = 72 + 25 + row * (304 + 25)
        player_photo = createImage(photo_x, photo_y, 170, 250)
        loadImage(current_player[1], player_photo); setScaleImageToFrame(1, 1, player_photo)
        
        photo_credit = "Photo: " + current_player[7].replace("\n", "")
        photo_credit_length = len(photo_credit)
        photo_credit_width = 3.0 * photo_credit_length + 2.5
        photo_credit_banner = createRect(photo_x + 170.0 - photo_credit_width, photo_y + 250 - 8, photo_credit_width, 8)
        setFillColor("NJCAA Blue", photo_credit_banner); setLineColor("None", photo_credit_banner); setFillTransparency(0.70, photo_credit_banner)
        
        
        photo_credit_text = createText(photo_x + 170.0 - photo_credit_width, photo_y + 250 - 8 + 1.5, photo_credit_width, 10)
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
        
        stat_banner_width = 33
        stat_banner_height = 24
        ellipse_width = stat_banner_width
        ellipse_height = ellipse_width / 2
        stat_banner_ellipse = createEllipse(banner_x + 133, (photo_y + stat_banner_height - ellipse_height / 2), ellipse_width, ellipse_height)
        setFillColor("White", stat_banner_ellipse); setLineColor("None", stat_banner_ellipse)
        
        stat_banner = createRect(banner_x + 133, photo_y, stat_banner_width, stat_banner_height)
        setFillColor("White", stat_banner); setLineColor("None", stat_banner)
        stat_text = createText(banner_x + 133, photo_y + 6, stat_banner_width, stat_banner_height)
        insertText(current_player[6] + "\n" + "kills", -1, stat_text)
        setFont("News of the World Wide Italic", stat_text); setFontSize(14, stat_text)
        setLineSpacing(10, stat_text); setTextAlignment(ALIGN_CENTERED, stat_text); setTextColor("NJCAA Blue", stat_text)
        
        
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
        
        if (page == 0 and col == 1 and row == 1):
          player_table_header = createRect(banner_x + 170 + 15, photo_y, 170, 24)
          setFillColor("NJCAA Blue", player_table_header); setLineColor("NJCAA Blue", player_table_header)
          
          table_title = createText(banner_x + 170 + 15, photo_y + 4.5, 170, 24)
          insertText("Matches with 20+ kills", -1, table_title)
          setTextColor("White", table_title)
          setFont("Playball Regular", table_title); setFontSize(17, table_title); setTextAlignment(ALIGN_CENTERED, table_title)
          
          num_lines = len(open("./Club_400_kills_20plus_kills_matches_2019_2020.csv").readlines()) - 1
          
          with open("./Club_400_kills_20plus_kills_matches_2019_2020.csv") as f:
            next(f) # skip headers row
            line_counter = 0
            line_height = 17
            for idx in range(num_lines):
              line_ypos = photo_y + 24 + line_counter * line_height
              line_background = createRect(banner_x + 170 + 15, line_ypos, 170, line_height)
              if line_counter % 2 == 0: line_color = "White"
              else: line_color = "Darker Gray"
              setFillColor(line_color, line_background); setLineColor(line_color, line_background)
              line_counter += 1
              
          player_frame_1 = createText(banner_x + 174 + 15, photo_y + 24 + 4, 130, 180)
          stat_frame_1 = createText(banner_x + 174 + 15 + 130, photo_y + 24 + 4, 30, 180)
          
          with open("./Club_400_kills_20plus_kills_matches_2019_2020.csv") as f:
            next(f) # skip headers row
            line_counter = 0
            for line in f:
              current_line_list = line.split(",")
              insertText(current_line_list[0] + "\n", -1, player_frame_1)
              insertText(current_line_list[1], -1, stat_frame_1)
              line_counter += 1
            insertText("\n", -1, stat_frame_1)
            
          setFont("Asimov Print C", player_frame_1); setFontSize(11, player_frame_1)
          setTextColor("NJCAA Blue", player_frame_1); setLineSpacing(17.05, player_frame_1)
          setTextAlignment(ALIGN_LEFT, player_frame_1)
          
          setFont("Asimov Print C", stat_frame_1); setFontSize(11, stat_frame_1)
          setTextColor("NJCAA Blue", stat_frame_1); setLineSpacing(17.05, stat_frame_1)
          setTextAlignment(ALIGN_RIGHT, stat_frame_1)
                        
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
  