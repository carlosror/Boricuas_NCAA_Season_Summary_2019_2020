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
with open("LAI_action_UAGM.csv") as f:
  next(f) # skip headers row
  for line in f:
    current_line_list = line.split(",")
    full_name = current_line_list[0].split()
    player_name = ""
    for name_part in full_name:
      player_name += name_part + " "
    player_name = player_name.rstrip()
    if (player_name in players_names_list): 
      player_name_count = sum([1 for plyr in players_names_list if plyr == player_name])
      image_filename = "./Puerto_Rico/LAI_action/" + player_name.replace(" ", "_") + "_" + str(player_name_count + 1) + ".jpg"
    else:
      image_filename = "./Puerto_Rico/LAI_action/" + player_name.replace(" ", "_") + ".jpg"
            
    # barreto_vazquez = "Paulina Barreto & Adriana Vázquez"
    # barreto_ayala_rivera = "Paulina Barreto & Jovyrelis Ayala (R.U.M.) & Stephanie Rivera"
    
    player_school = current_line_list[1]
    school_city = current_line_list[2]
    school_league = current_line_list[3]
    school_division = current_line_list[4]
    photo_credit = current_line_list[5]
    
    single_player_list = [player_name, image_filename, player_school, school_city, school_league, school_division, photo_credit]
    players_list.append(single_player_list)
    players_names_list.append(player_name)


if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
  defineColor("UAGM", 5, 239, 207, 13)
  
  # top_right_rect = createRect(306, 36, 306, 180)
  # setFillColor("NJCAA Gray", top_right_rect); setLineColor("NJCAA Gray", top_right_rect)
  # second_rect = createRect(0, 216, 306, 180)
  # setFillColor("NJCAA Gray", second_rect); setLineColor("NJCAA Gray", second_rect)
  # third_rect = createRect(306, 396, 306, 180)
  # setFillColor("NJCAA Gray", third_rect); setLineColor("NJCAA Gray", third_rect)
  # top_left_rect = createRect(0, 576, 306, 180)
  # setFillColor("NJCAA Gray", top_left_rect); setLineColor("NJCAA Gray", top_left_rect)
  
  num_players = len(players_list)
  if (num_players % 8) == 0: 
    num_pages = (num_players / 8) 
  else: 
    num_pages = (num_players / 8) + 1
  player_count = 0
  for page in range(num_pages):
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("UAGM", top_rect); setLineColor("UAGM", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("UAGM", bottom_rect); setLineColor("UAGM", bottom_rect)
    center_rect = createRect(0, 36, 612, 720)
    setFillColor("White", center_rect); setLineColor("White", center_rect)
    
    page_header = createText(36, 5, 540, 36)
    setText("Universidad Ana G. Méndez", page_header)
    setTextColor("White", page_header)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
    setTextAlignment(ALIGN_CENTERED, page_header)
    
    years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
    years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
    setTextColor("White", years1); setTextColor("White", years2)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
    setLineSpacing(7, years1); setLineSpacing(7, years2)  
        
    for row in range(4):
      for col in range(2):
        current_player = players_list[player_count]
        photo_width = 270; photo_height = 177
        photo_x = 38 + col * (photo_width)
        # photo_y = 36 + 20 + row * (250 + 100)
        photo_y = 36 + row * (photo_height + 4)
        player_photo = createImage(photo_x, photo_y, photo_width, photo_height)
        loadImage(current_player[1], player_photo); setScaleImageToFrame(1, 1, player_photo)
        
        league_x = photo_x + 15; league_y = photo_y + 15
        player_league = createImage(league_x, league_y, 25, 25)
        loadImage("./Division_logos/" + current_player[4].replace(" ", "_").replace("\n","") + "_logo.png", player_league); setScaleImageToFrame(1, 1, player_league)
        
        if current_player[5] == "NCAA DII":
          player_division = createImage(league_x, league_y + 30, 25, 25)
          loadImage("./Division_logos/" + current_player[5].replace(" ", "_").replace("\n","") + "_logo.png", player_division); setScaleImageToFrame(1, 1, player_division)
                
        banner_width = 180; banner_height = 30
        banner_x = photo_x + (photo_width - banner_width) / 2.0
        # if (current_player[0] in [barreto_vazquez, barreto_ayala_rivera]):
          # banner_width = 265.54; banner_x = photo_x
        banner_y = photo_y + (photo_height - banner_height)
        player_banner = createRect(banner_x, banner_y, banner_width, banner_height)
        setFillColor("White", player_banner); setLineColor("None", player_banner)
        
        
        logo_name = current_player[2].replace(" ", "_")
        # if (current_player[0] in [barreto_ayala_rivera]):
          # logo_name = "Recinto Universitario de Río Piedras".replace(" ", "_")
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
        # max_logo_width = 35.0
        # if (current_player[0] in [barreto_vazquez, barreto_ayala_rivera]):
          # player_name = createText(banner_x + logo_width + 1, banner_y + 3, banner_width - 2 * logo_width, banner_height)
        # else:
        player_name = createText(banner_x + logo_width + 1, banner_y + 3, banner_width - logo_width, banner_height)
        insertText(current_player[0] + "\n", -1, player_name)
        setFont("Playball Regular", player_name);
        # if (current_player[0] in [barreto_vazquez]): setFontSize(13, player_name)
        # elif (current_player[0] in [barreto_ayala_rivera]): setFontSize(7.5, player_name)
        setFontSize(15, player_name)
        name_length = len(unicode(current_player[0] + "\n"))
        player_school_and_state = current_player[2] + " | " + current_player[3]
        # if (current_player[0] in [maldonado_justiniano_lopez, maldonado_arguello_burgos, lugo_maldonado_arguello]):
          # player_school_and_state = current_player[2]
        school_and_state_length = len(unicode(player_school_and_state))
        insertText(player_school_and_state, -1, player_name)
        selectText(name_length, school_and_state_length, player_name)
        setFont("Asimov Print C", player_name)
        selectText(name_length, school_and_state_length, player_name); setFontSize(6.7, player_name)
        setTextColor("NJCAA Blue", player_name)
        setLineSpacing(11, player_name)
        setTextAlignment(ALIGN_CENTERED, player_name)
        
        # if (current_player[0] in [barreto_ayala_rivera]):
          # logo_name_2 = "Recinto Universitario de Mayagüez".replace(" ", "_")
          # if (school_logos_dict[logo_name_2] < 0.7):
            # logo_width = 33.0
            # logo_height = min(logo_width * school_logos_dict[logo_name_2], 28)
          # else:
            # logo_height = 28.0
            # logo_width = min(logo_height / school_logos_dict[logo_name_2], 33)
          # logo_ypos = (banner_y + (banner_height - logo_height) / 2.0)
          # school_logo = createImage(banner_x + banner_width - logo_width - 1, logo_ypos, logo_width, logo_height)
          # loadImage("./School_Logos/" + logo_name_2 + ".gif", school_logo); setScaleImageToFrame(1, 1, school_logo)
        
        
        photo_credit = "Photo: " + current_player[6].replace("\n", "")
        photo_credit_length = len(photo_credit)
        photo_credit_width = 4.0 * photo_credit_length + 6.0
        photo_credit_banner = createRect(photo_x + 265.54 - photo_credit_width, photo_y, photo_credit_width, 10)
        setFillColor("NJCAA Blue", photo_credit_banner); setLineColor("None", photo_credit_banner); setFillTransparency(0.70, photo_credit_banner)
        
        
        photo_credit_text = createText(photo_x + 265.54 - photo_credit_width, photo_y + 1.5, photo_credit_width, 12)
        setText(photo_credit, photo_credit_text)
        setTextColor("White", photo_credit_text); setFont("Asimov Print C", photo_credit_text); setFontSize(8, photo_credit_text)
        setTextAlignment(ALIGN_CENTERED, photo_credit_text)
                      
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
  