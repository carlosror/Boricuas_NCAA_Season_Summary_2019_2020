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

tourney_logos_dict = {}
with open("./Tournament_Logos/filesizes_png.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    tourney_logos_dict[current_line_list[0]] = float(current_line_list[2]) / float (current_line_list[1])
                     
banner_colors_dict = {"Florida Memorial University": [0, 0, 0, 0], "University of Saint Mary": [0, 0, 0, 0], "Xavier University of Louisiana": [0, 0, 0, 255], 
                      "College of Coastal Georgia": [0, 0, 0, 0], "Fisher College": [0, 0, 0, 0], "Cal State University Los Angeles": [0,0,0,0], 
                      "Bloomfield College": [int(0.043*255), int(0.078*255), int(0.737*255), int(0.0039*255)], "Lasell University": [0,0,0,0], 
                      "Western Connecticut State University": [0,0,0,0], "Notre Dame of Maryland University": [0,0,0,0], "Manhattanville College": [0,0,0,0], 
                      "Bethany College":[int(0.035*255), int(0.071*255), int(0.898*255), int(0.012*255)], "Indiana University Northwest": [int(0.094*255), int(0.961*255), int(0.596*255), int(0.2*255)], 
                      "Edward Waters College":[int(0.671*255), int(0.969*255), int(0.016*255), int(0.031*255)], "St. Francis College": [0,0,0,0], 
                      "Delaware State University":[0,0,0,0], "American International College": [0,0,0,0], "Berea College":[0,0,0,0], 
                      "Oklahoma Wesleyan University":[int(0.325*255), int(0.906*255), int(0.42*255), int(0.482*255)], 
                      "University of California Irvine": [int(0.91*255), int(0.792*255), int(0.09*255), int(0.678*255)], "Saint Anselm College": [0,0,0,0], 
                      "Mercy College": [0,0,0,0], "University of the Sciences": [0,0,0,0], "University of Missouri": [0,0,0,0], 
                      "Saint Peter's University": [0,0,0,0], "Savannah State University": [0,0,0,0],
                      "Valdosta State University":[0,0,0,0], "Florida Technical College":[0,0,0,0], "Elms College":[0,0,0,0], "Keiser University":[0,0,0,0], 
                      "St. Andrews University":[0,0,0,0], "North Carolina Central University":[0,0,0,0], "University of Tampa": [0,0,0,0], "Springfield College": [0,0,0,0], 
                      "Catholic University of America": [0,0,0,0], "Morgan State University": [0,0,0,0], "University of North Florida": [0,0,0,0], "The Citadel": [0,0,0,0], 
                      "Florida International University": [0,0,0,0], "North Carolina A&T": [0,0,0,0], "Tennessee State University": [0,0,0,0], "Coppin State University": [0,0,0,0], 
                      "Quinnipiac University": [0,0,0,0], "University of Evansville": [0,0,0,0], "Manhattan College": [0,0,0,0], "Southern Illinois University": [0,0,0,0], 
                      "Goldey-Beacom College": [0,0,0,0], "Maine Maritime Academy": [0,0,0,0], "Dickinson College": [0,0,0,0], "University of Saint Joseph's": [0,0,0,0], 
                      "Pratt Institute": [0,0,0,0], "Chowan University": [0,0,0,0], "Rutgers University - Newark": [0,0,0,0], "Clark University": [0,0,0,0]}

banner_text_colors_dict = {"Florida_Memorial_University": [int(0.878*255), int(0.749*255), 0, 0], "University_of_Saint_Mary": [int(0.882*255), int(0.722*255), int(0.212*255), int(0.659*255)], 
                           "Xavier_University_of_Louisiana": [0, 0, 0, 0], "College_of_Coastal_Georgia": [int(0.808*255), int(0.741*255), int(0.012*255), int(0.0235*255)],
                           "Fisher_College": [int(0.788*255), int(0.761*255), int(0.098*255), int(0.177*255)],
                           "Cal_State_University_Los_Angeles": [0,0,0,255], "Bloomfield_College": [int(0.408*255), int(0.804*255), int(0.455*255), int(0.435*255)], 
                           "Lasell_University": [int(0.941*255), int(0.831*255), int(0.059*255), int(0.428*255)], 
                           "Western_Connecticut_State_University": [int(0.906*255), int(0.737*255), int(0.227*255), int(0.486*255)], 
                           "Manhattanville_College": [int(0.118*255), int(0.965*255), int(0.608*255), int(0.239*255)], "Notre_Dame_of_Maryland_University": [int(0.925*255), int(0.737*255), int(0.125*255), int(0.365*255)], 
                           "Bethany_College": [int(0.89*255), int(0.635*255), int(0.008*255), int(0.016*255)], "Indiana_University_Northwest": [0,0,0,0], 
                           "Edward_Waters_College": [0,0,0,0], "St._Francis_College": [int(0.016*255), int(0.941*255), int(0.741*255), int(0.02*255)], 
                           "Delaware_State_University":[0,0,0,255], "American_International_College": [0,0,0,255], "Berea_College":[int(0.851*255), int(0.537*255), int(0.11*255), int(0.212*255)], 
                           "Oklahoma_Wesleyan_University":[0,0,0,0], "University_of_California_Irvine":[0,0,0,int(0.078*255)], "Saint_Anselm_College":[int(0.925*255), int(0.718*255), int(0.188*255), int(0.588*255)], 
                           "Mercy_College": [int(0.91*255), int(0.729*255), int(0.173*255), int(0.428*255)], "University_of_the_Sciences": [int(0.212*255), int(0.933*255), int(0.353*255), int(0.471*255)], 
                           "University_of_Missouri": [0,0,0,255], "Saint_Peter's_University":[int(0.82*255), int(0.455*255), int(0.008*255), int(0.016*255)], "Savannah_State_University": [int(0.0*255), int(0.78*255), int(1.0*255), int(0.0*255)], 
                           "Valdosta_State_University":[int(0.004*255), int(0.957*255), int(0.961*255), int(0.098*255)], "Florida_Technical_College": [0,0,0,255], 
                           "Elms_College":[int(0.796*255), int(0.247*255), int(0.749*255), int(0.643*255)], "Keiser_University":[int(0.886*255), int(0.796*255), int(0.153*255), int(0.416*255)], 
                           "St._Andrews_University": [int(0.902*255), int(0.875*255), int(0.047*255), int(0.153*255)], "North_Carolina_Central_University": [int(0.239*255), int(0.906*255), int(0.643*255), int(0.357*255)], 
                           "University_of_Tampa": [int(0.039*255), int(0.957*255), int(0.741*255), int(0.129*255)], "Springfield_College": [int(0.098*255), int(0.976*255), int(0.639*255), int(0.38*255)], 
                           "Catholic_University_of_America": [int(0.027*255), int(0.925*255), int(0.929*255), int(0.204*255)], "Morgan_State_University": [int(0.91*255), int(0.702*255), int(0.078*255), int(0.165*255)], 
                           "University_of_North_Florida": [int(0.918*255), int(0.788*255), int(0.106*255), int(0.612*255)], "The_Citadel": [int(0.894*255), int(0.804*255), int(0.145*255), int(0.475*255)], 
                           "Florida_International_University": [int(0.941*255), int(0.792*255), int(0.102*255), int(0.396*255)], "North_Carolina_A&T": [int(0.914*255), int(0.686*255), int(0.137*255), int(0.341*255)], 
                           "Tennessee_State_University": [int(0.906*255), int(0.678*255), int(0.016*255), int(0.353*255)], "Coppin_State_University": [int(0.922*255), int(0.702*255), int(0.204*255), int(0.482*255)], 
                           "Quinnipiac_University": [int(0.882*255), int(0.722*255), int(0.212*255), int(0.659*255)], "University_of_Evansville": [int(0.816*255), int(0.957*255), int(0.016*255), int(0.055*255)], 
                           "Manhattan_College": [int(0.812*255), int(0.22*255), int(0.827*255), int(0.286*255)], "Southern_Illinois_University": [int(0.349*255), int(0.886*255), int(0.447*255), int(0.456*255)], 
                           "Goldey-Beacom_College": [int(0.937*255), int(0.78*255), int(0.118*255), int(0.447*255)], "Maine_Maritime_Academy": [int(0.82*255), int(0.565*255), int(0.027*255), int(0.051*255)], 
                           "Dickinson_College": [int(0.004*255), int(0.941*255), int(0.843*255), int(0.012*255)], "University_of_Saint_Joseph's": [int(0.941*255), int(0.792*255), int(0.102*255), int(0.396*255)], 
                           "Pratt_Institute": [int(0.475*255), int(0.443*255), int(0.384*255), int(0.89*255)], "Chowan_University": [int(0.835*255), int(0.498*255), int(0.016*255), int(0.028*255)], 
                           "Rutgers_University_-_Newark": [int(0.008*255), int(0.945*255), int(0.949*255), int(0.067*255)], "Clark_University": [int(0.0*255), int(0.863*255), int(0.835*255), int(0.0*255)]}
players_list = []
players_names_list = []
with open("National_tournaments.csv") as f:
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
        image_filename = "./National_Tournaments/" + first_name + "_" + full_name[1] + "_" + full_name[2] + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./National_Tournaments/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
    else:
      player_name = first_name + " " + first_last_name
      if (player_name in players_names_list): 
        player_name_count = sum([1 for plyr in players_names_list if plyr == player_name])
        image_filename = "./National_Tournaments/" + first_name + "_" + first_last_name + "_" + str(player_name_count + 1) + ".jpg"
      else:
        image_filename = "./National_Tournaments/" + first_name + "_" + first_last_name + ".jpg"
      
    player_school = current_line_list[1] 
    school_state = current_line_list[2]
    school_division = current_line_list[3]
    tournament = current_line_list[4]
    outcome = current_line_list[5]
    
    single_player_list = [player_name, image_filename, player_school, school_state, school_division, tournament, outcome]
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
    page_title = "National Tournaments Participants\n"
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
        photo_y = 36 + 7 + row * (250 + 106)
        player_photo = createImage(photo_x, photo_y, 170, 250)
        loadImage(current_player[1], player_photo); setScaleImageToFrame(1, 1, player_photo)
        
        division_x = photo_x + 5
        if (current_player[4].replace("\n","") in ["NCAA DI", "NCAA DII", "NCAA DIII", "NJCAA DI", "NJCAA DII"]):
          division_y = photo_y + 5
          player_division = createImage(division_x, division_y, 25, 25)
        else:
          division_y = photo_y + 10
          player_division = createImage(division_x, division_y, 25, 12)
        loadImage("./Division_logos/" + current_player[4].replace(" ", "_").replace("\n","") + "_logo.png", player_division); setScaleImageToFrame(1, 1, player_division)
                
        banner_x = photo_x
        banner_y = photo_y + (250 * 0.8)
        player_banner = createRect(banner_x, banner_y, 170, 250 * 0.15)
        setFillColor("White", player_banner); setLineColor("None", player_banner)
        setFillTransparency(0.70, player_banner)
        
        logo_name = current_player[2].replace(" ", "_")
        logo_width = 45.0
        logo_height = school_logos_dict[logo_name] * logo_width
        logo_ypos = (banner_y + (250 * 0.15) / 2 - logo_height / 2.0)
        school_logo = createImage(banner_x + 2, logo_ypos, logo_width, logo_height)
        loadImage("./School_Logos/" + logo_name + ".gif", school_logo); setScaleImageToFrame(1, 1, school_logo)
        
        vocales_acentos = ["Á", "É", "Í", "Ó", "Ú", "Ñ"]
        if any(x in unicode(current_player[0]).upper() for x in vocales_acentos): player_name_ypos = banner_y + 3
        else: player_name_ypos = banner_y + 5
        player_name = createText(banner_x + 2 + logo_width, player_name_ypos, 170 - 2 - logo_width, 250 * 0.15)
        insertText(unicode(current_player[0]).upper() + "\n", -1, player_name)
        setFont("Asimov Print C", player_name); setFontSize(9.4, player_name)
        name_length = getTextLength(player_name)
        player_school = current_player[2]
        school_length = len(player_school) + 1
        insertText(unicode(player_school).upper() + "\n", -1, player_name)
        selectText(name_length, school_length, player_name)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_name)
        selectText(name_length, len(player_school), player_name); setFontSize(5.5, player_name)
        school_state = current_player[3]
        insertText(school_state, -1, player_name)
        selectText(name_length + school_length, len(school_state), player_name)
        setFont("Playball Regular", player_name)
        selectText(name_length + school_length, len(school_state), player_name); setFontSize(10, player_name)
        setTextColor("NJCAA Blue", player_name)
        setLineSpacing(11, player_name)
        setTextAlignment(ALIGN_CENTERED, player_name)
        
        # player_stat_background_height = 39.0
        # player_stat_background = createRect(banner_x + 0.5, photo_y + 250, 169, player_stat_background_height)
        # setFillColor("White", player_stat_background); setLineColor("White", player_stat_background)
        
        # player_stat_h = 38
        # player_stat = createText(banner_x, photo_y + 250 + 5, 170, player_stat_h)
        # insertText(current_player[2] + "\n", -1, player_stat)
        # setFont("News of the World Wide Italic", player_stat); setFontSize(18, player_stat)
        # stat_length = getTextLength(player_stat)
        # player_rank = current_player[3]
        # if player_rank == "1": player_rank = "1st"
        # elif player_rank == "2": player_rank = "2nd"
        # elif player_rank == "3": player_rank = "3rd"
        # else: player_rank = str(player_rank) + "th"
        # rank_length = len(player_rank) + 1
        # insertText(player_rank + "\n", -1, player_stat)
        # selectText(stat_length, rank_length, player_stat); setFontSize(28, player_stat)
        # setTextColor("NJCAA Blue", player_stat)
        # setLineSpacing(20, player_stat); setTextAlignment(ALIGN_CENTERED, player_stat)
        
        player_tourney_background_height = 77.0
        player_tourney_background = createRect(banner_x + 0.5, photo_y + 250, 169, player_tourney_background_height)
        setFillColor("Darker Gray", player_tourney_background); setLineColor("Darker Gray", player_tourney_background)
        
        tournament_logo_h = 50.0
        tournament_img = current_player[5].replace(" ", "_")
        # using the min() function here b/c the Conf-USA logo is very short and wide
        player_tourney_img_w = min(tournament_logo_h / tourney_logos_dict[tournament_img], 170.0)
        tournament_logo = createImage(banner_x + (170 - player_tourney_img_w) / 2.0, photo_y + 250 + 3, player_tourney_img_w, tournament_logo_h)
        loadImage("./Tournament_Logos/" + tournament_img + ".png", tournament_logo); setScaleImageToFrame(1, 1, tournament_logo)
        
        player_tourney_frame = createText(banner_x, photo_y + 250 + 5 + tournament_logo_h, 170, 22)
        player_tourney = current_player[5]
        insertText(player_tourney, -1, player_tourney_frame)
        setTextColor("NJCAA Blue", player_tourney_frame)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_tourney_frame); setFontSize(9, player_tourney_frame)
        setLineSpacing(11, player_tourney_frame); setTextAlignment(ALIGN_CENTERED, player_tourney_frame)
        
        player_tourney_outcome_banner_height = 20.0
        player_tourney_outcome_banner = createRect(banner_x + 0.5, photo_y + 250 + player_tourney_background_height + 1, 169, player_tourney_outcome_banner_height)
        setFillColor("White", player_tourney_outcome_banner); setLineColor("White", player_tourney_outcome_banner)
        
        player_tourney_outcome_h = 20.0
        player_tourney_frame = createText(banner_x, photo_y + 250 + player_tourney_background_height + 7, 170, 20)
        player_tourney_outcome = current_player[6]
        insertText(player_tourney_outcome, -1, player_tourney_frame)
        setTextColor("NJCAA Blue", player_tourney_frame)
        setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_tourney_frame); setFontSize(9, player_tourney_frame)
        setLineSpacing(11, player_tourney_frame); setTextAlignment(ALIGN_CENTERED, player_tourney_frame)
        
        # line1 = createLine(banner_x + 0.25, photo_y + 250 - 0.5, banner_x, photo_y + 250 + player_stat_background_height + player_conf_background_height + 0.5)
        # line2 = createLine(banner_x - 0.25 + 170, photo_y + 250 - 0.5, banner_x + 170, photo_y + 250 + player_stat_background_height + player_conf_background_height + 0.5)
        # line3 = createLine(banner_x, photo_y + 250 + player_stat_background_height + player_conf_background_height + 0.5, banner_x + 0.25 + 170, photo_y + 250 + player_stat_background_height + player_conf_background_height + 0.5)
        # setLineWidth(0.5, line1); setLineWidth(0.5, line2); setLineWidth(0.5, line3)
      
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
  