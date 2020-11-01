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
with open("All_Academic_2019_2020.csv") as f:
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
        image_filename = "./" + current_line_list[4].replace(" ", "_").replace("\n","") + "_mugshots_2/"  + first_name + "_" + full_name[1] + "_" + full_name[2] + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./" + current_line_list[4].replace(" ", "_").replace("\n","") + "_mugshots_2/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
    else:
      player_name = first_name + " " + first_last_name
      if (player_name in players_names_list): 
        player_name_count = sum([1 for plyr in players_names_list if plyr == player_name])
        image_filename = "./" + current_line_list[4].replace(" ", "_").replace("\n","") + "_mugshots_2/" + first_name + "_" + first_last_name + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./" + current_line_list[4].replace(" ", "_").replace("\n","") + "_mugshots_2/" + first_name + "_" + first_last_name + ".jpg"
      
    player_school = current_line_list[1]
    school_state = current_line_list[2]
    if current_line_list[2] == "Washington D.C.": school_state = "Washington, D.C."
    player_conf = current_line_list[3]
    school_division = current_line_list[4]
    # Beach VB players:
    if player_name in ["Keniah Rivera", "Joise Maldonado", "Génesis Benítez"]: school_division = current_line_list[4].replace(" BVB", "")
    player_major = current_line_list[5]
    player_GPA = current_line_list[6]
    player_award = current_line_list[7]
    
    single_player_list = [player_name, image_filename, player_school, school_state, player_conf, school_division, player_major, player_award, player_GPA]
    players_list.append(single_player_list)
    players_names_list.append(player_name)


if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
    
  num_players = len(players_list)
  if (num_players % 12) == 0: 
    num_pages = (num_players / 12) 
  else: 
    num_pages = (num_players / 12) + 1
  player_count = 0
  for page in range(num_pages):
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    center_rect = createRect(0, 36, 612, 720)
    setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    
    page_header = createText(36, 9, 540, 36)
    setText("Academic All-Stars", page_header)
    setTextColor("White", page_header)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
    setTextAlignment(ALIGN_CENTERED, page_header)
    
    if page == 0:
      header_asterisk = createText(434, 9, 12, 36)
      setText("*", header_asterisk); setTextColor("White", header_asterisk); setFontSize(18, header_asterisk)
      
      footer_asterisk = createText(36, 758, 4, 34)
      setText("*", footer_asterisk); setTextColor("White", footer_asterisk); setFontSize(7, footer_asterisk)
      
      footnote_frame = createText(40, 758, 536, 35)
      footnote = "Players that were recognized by their conference for their performance in the classroom. All conferences of four-year institutions " \
                 "require athletes to have a 3.00 GPA as a bare minimum to receive an award, and several conferences set the bar higher: 3.20, 3.30, 3.40, " \
                 "and, in the case of The Sun Conference, a 3.50 GPA as a minimum. Lina Bernier was awarded Conference USA's Commmissioner's Medal (GPA > 3.75) for the" \
                 "the 5th year in a row, while Sharlissa de Jesús earned Southern Conference's Commmissioner's Medal (GPA > 3.80). The NJCAA has 3 tiers of " \
                 "academic awards: 3rd team (GPA > 3.60), 2nd team (GPA > 3.80), and 1st team (GPA = 4.00)"
      setText(footnote, footnote_frame); setTextColor("White", footnote_frame); setFontSize(7, footnote_frame); setLineSpacing(9, footnote_frame)
    
    years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
    years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
    setTextColor("White", years1); setTextColor("White", years2)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
    setLineSpacing(7, years1); setLineSpacing(7, years2)
    
    for row in range(3):
      for col in range(4):
        current_player = players_list[player_count]
        photo_x = 36 + col * (132 + 4)
        # photo_y = 36 + 20 + row * (250 + 100)
        photo_y = 36 + 18 + row * (176 + 58)
        player_photo = createImage(photo_x, photo_y, 132, 176)
        loadImage(current_player[1], player_photo); setScaleImageToFrame(1, 1, player_photo)
        
        division_x = photo_x + 5
        if (current_player[5].replace("\n","") in ["NCAA DI", "NCAA DII", "NCAA DIII", "NJCAA DI", "NJCAA DII"]):
          division_y = photo_y + 5
          player_division = createImage(division_x, division_y, 25, 25)
        else:
          division_y = photo_y + 10
          player_division = createImage(division_x, division_y, 25, 12)
        loadImage("./Division_logos/" + current_player[5].replace(" ", "_").replace("\n","") + "_logo.png", player_division); setScaleImageToFrame(1, 1, player_division)
                
        banner_x = photo_x
        banner_y = photo_y + 122
        player_banner = createRect(banner_x, banner_y, 132, 38)
        setFillColor("White", player_banner); setLineColor("None", player_banner)
        setFillTransparency(0.70, player_banner)
        
        # academic_logo = createImage(banner_x + 2, banner_y + 2, 40, 40)
        # loadImage("./All_Academic/All_Academic_logo.png", academic_logo); setScaleImageToFrame(1, 1, academic_logo)
        
        vocales_acentos = ["Á", "É", "Í", "Ó", "Ú", "Ñ"]
        # if any(x in unicode(current_player[0]).upper() for x in vocales_acentos): player_name_ypos = banner_y + 2
        player_name_ypos = banner_y + 4
        player_name = createText(banner_x, player_name_ypos, 132, 38)
        insertText(unicode(current_player[0]) + "\n", -1, player_name)
        setFont("Asimov Print C", player_name); setFontSize(11, player_name)
        name_length = getTextLength(player_name)
        player_school = current_player[2]
        school_length = len(player_school) + 1
        insertText(unicode(player_school).upper() + "\n", -1, player_name)
        selectText(name_length, school_length, player_name)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_name)
        selectText(name_length, len(player_school), player_name); setFontSize(6.7, player_name)
        school_state = current_player[3]
        insertText(school_state, -1, player_name)
        selectText(name_length + school_length, len(school_state), player_name)
        setFont("Playball Regular", player_name)
        selectText(name_length + school_length, len(school_state), player_name); setFontSize(11, player_name)
        # banner_text_color_cmyk = banner_text_colors_dict[current_player[5].replace(" ", "_")]
        # defineColor(current_player[5].replace(" ", "_"), banner_text_color_cmyk[0], banner_text_color_cmyk[1], banner_text_color_cmyk[2], banner_text_color_cmyk[3])
        setTextColor("NJCAA Blue", player_name)
        setLineSpacing(11, player_name)
        setTextAlignment(ALIGN_CENTERED, player_name)
        
        player_major_background_height = 34
        player_major_background = createRect(banner_x + 0.5, photo_y + 176 - 10, 131, player_major_background_height)
        setFillColor("White", player_major_background); setLineColor("White", player_major_background)
        
        player_academics_h = 35
        offset = 2.5
        if current_player[6] == "": offset = 5
        player_academics = createText(banner_x, photo_y + 176 - 10 + offset, 132, player_academics_h)
        insertText(current_player[6] + "\n", -1, player_academics)
        setFont("Playball Regular", player_academics); setFontSize(11, player_academics)
        major_length = getTextLength(player_academics)
        player_award = current_player[7]
        award_length = len(player_award)
        insertText(player_award + "\n", -1, player_academics)
        # page_debug = createText(banner_x, photo_y + 176 + 3 + player_major_background_height, 132, 24)
        # setText("\n" + str(major_length) + " " + str(award_length), page_debug)
        selectText(major_length, award_length, player_academics); setFontSize(7.5, player_academics)
        selectText(major_length, award_length, player_academics); setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_academics)
        player_GPA = current_player[8]
        GPA_length = len("Minimum GPA: " + player_GPA + "\n")
        insertText("Minimum GPA: " + player_GPA, -1, player_academics)
        selectText(major_length + award_length, GPA_length, player_academics); setFontSize(9.0, player_academics)
        selectText(major_length + award_length, GPA_length, player_academics); setFont("Asimov Print C", player_academics)
        setTextColor("NJCAA Blue", player_academics)
        setLineSpacing(10, player_academics); setTextAlignment(ALIGN_CENTERED, player_academics)
        
        if (current_player[0] == "Cecilia Thon"):
          award_asterisk = createText(294, 711, 12, 36)
          setText("*", award_asterisk); setTextColor("NJCAA Blue", award_asterisk); setFontSize(12, award_asterisk)
      
          footer_asterisk = createText(36, 758, 4, 34)
          setText("*", footer_asterisk); setTextColor("White", footer_asterisk); setFontSize(7, footer_asterisk)
      
          footnote_frame = createText(40, 758, 536, 35)
          footnote = "Commissioner’s Academic Excellence Award" 
          setText(footnote, footnote_frame); setTextColor("White", footnote_frame); setFontSize(7, footnote_frame); setLineSpacing(9, footnote_frame)
          
        if (current_player[0] == "Laura Rojas"):
          award_asterisk = createText(430, 711, 12, 36)
          setText("**", award_asterisk); setTextColor("NJCAA Blue", award_asterisk); setFontSize(12, award_asterisk)
      
          footer_asterisk = createText(36, 770, 4, 34)
          setText("**", footer_asterisk); setTextColor("White", footer_asterisk); setFontSize(7, footer_asterisk)
      
          footnote_frame = createText(40, 770, 536, 35)
          footnote = "Presidents' Council Academic Excellence Award" 
          setText(footnote, footnote_frame); setTextColor("White", footnote_frame); setFontSize(7, footnote_frame); setLineSpacing(9, footnote_frame)
        
        
        player_conf_background_height = 24.0
        player_conf_background = createRect(banner_x + 0.5, photo_y + 176 - 10 + player_major_background_height, 131, player_conf_background_height)
        setFillColor("Darker Gray", player_conf_background); setLineColor("Darker Gray", player_conf_background)
        
        player_conf_logo_w = 33.0
        player_conf_img = current_player[4].replace(" ", "_")
        player_conf_logo_h = min(player_conf_logo_w * conf_logos_dict[player_conf_img], 24.0)
        conf_logo = createImage(banner_x, photo_y + 176 - 10 + player_major_background_height + (player_conf_background_height - player_conf_logo_h) / 2.0, player_conf_logo_w, player_conf_logo_h)
        loadImage("./Conference_Logos/" + player_conf_img + ".png", conf_logo); setScaleImageToFrame(1, 1, conf_logo)
        
        offset = 10.0
        if len(current_player[4]) > 26: offset = 2.5
        player_conf_frame = createText(banner_x + player_conf_logo_w + 1, photo_y + 176 - 10 + player_major_background_height + offset, 98, 19)
        # player_conf_array = current_player[4].split(" ")
        # player_conf_array_length = len(player_conf_array)
        # if (player_conf_array_length % 2) == 0: split_point = player_conf_array_length / 2
        # else: split_point = (player_conf_array_length / 2) + 1
        # player_conf = " ".join(player_conf_array[0:split_point]) + "\n" + " ".join(player_conf_array[split_point:])
        player_conf = current_player[4]
        # player_conf_length = len(player_conf)
        insertText(player_conf, -1, player_conf_frame)
        setTextColor("NJCAA Blue", player_conf_frame)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_conf_frame); setFontSize(6.1, player_conf_frame)
        setLineSpacing(11, player_conf_frame); setTextAlignment(ALIGN_CENTERED, player_conf_frame)
              
        player_count += 1
        if player_count == num_players: break
      if player_count == num_players: break
    if player_count == num_players: break
    # if page == 1: break
    
    
    # right_rect = createRect(576, 36, 36, 720)
    # setFillColor("NJCAA Gray", right_rect); setLineColor("NJCAA Gray", right_rect)
    # left_rect = createRect(0, 36, 36, 720)
    # setFillColor("NJCAA Gray", left_rect); setLineColor("NJCAA Gray", left_rect)
    newPage(-1)
  