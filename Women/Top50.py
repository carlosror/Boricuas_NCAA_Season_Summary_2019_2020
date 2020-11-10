#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

# Dictionary of logos' height/width aspect ratios. It is used to position the school logo
# There's no way to programatically adjust frame to image.
# The Python Scribus uses doesn;t have any image utilities like PIL so I could not
# figure out a way to determine the image's aspect ratio programatically. :|
school_logos_dict = {"American_International_College": 859.0/1200, "Bryant_&_Stratton_College": 648.0/648, "Cal_State_University_Los_Angeles": 1133.0/1200, 
                     "Clarendon_College":220.0/216, "Goldey-Beacom_College": 373.0/470, "University_of_Saint_Mary": 1229.0/1200, 
                     "Monroe_College": 190.0/260, "Manhattanville_College": 512.0/512, "Lasell_University": 363.0/250, "Laredo_College": 1000.0/1450, 
                     "Coffeyville_Community_College": 246.0/369, "Cowley_College": 172.0/186, "Florida_Memorial_University": 177.0/310, "The_Citadel": 705.0/1144, 
                     "Delaware_State_University": 912.0/1200, "Notre_Dame_of_Maryland_University": 587.0/1166, "Cisco_College": 307.0/558, 
                     "Fisher_College": 305.0/547, "Lake_Region_State_College": 938.0/945, "Allen_Community_College": 288.0/346, "University_of_Missouri": 685.0/1200, 
                     "Independence_Community_College": 532.0/548, "Santa_Fe_College": 216.0/307, "Polk_State_College": 119.0/250, "Daytona_State_College": 150.0/197, 
                     "College_of_Coastal_Georgia": 130.0/175, "St._Andrews_University": 132.0/165, "Western_Nebraska_Community_College": 543.0/799, 
                     "Florida_International_University": 588.0/593, "Southern_Illinois_University": 717.0/869, "Saint_Peter's_University": 251.0/326, 
                     "University_of_North_Florida": 235.0/248, "Florida_State_College_at_Jacksonville": 209.0/199, "Bethany_College": 227.0/214,
                     "Indiana_University_Northwest": 136.0/180, "Chestnut_Hill_College": 170.0/176, "University_of_Evansville": 435.0/440}

players_list = []
players_names_list = []
with open("Top50.csv") as f:
  next(f) # skip headers row
  for line in f:
    current_line_list = line.split(",")
    full_name = current_line_list[0].split()
    first_name = full_name[0]
    first_last_name = full_name[1]
    if (full_name[1] == "de" or full_name[1] == "La"):
      player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
      if (player_name in players_names_list): 
        image_filename = "./Top50/" + first_name + "_" + full_name[1] + "_" + full_name[2] + "_2" + ".jpg"
      else:
        image_filename = "./Top50/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
    else:
      player_name = first_name + " " + first_last_name
      if (player_name in players_names_list): 
        image_filename = "./Top50/" + first_name + "_" + first_last_name + "_2" + ".jpg"
      else:
        image_filename = "./Top50/" + first_name + "_" + first_last_name + ".jpg"
      
    player_stat = current_line_list[1] + " " + current_line_list[2]
    player_rank = current_line_list[3]
    player_school = current_line_list[4]
    school_state = current_line_list[5]
    school_division = current_line_list[6]
    photo_credit = current_line_list[7]
    
    hometown = current_line_list[6]
    single_player_list = [player_name, image_filename, player_stat, player_rank, player_school, school_division, school_state, photo_credit]
    players_list.append(single_player_list)
    players_names_list.append(player_name)

def text_frame(pos_x, pos_y, frame_width, frame_height, texts_list, fonts_list, font_sizes, color = "NJCAA Blue", alignment = ALIGN_CENTERED, line_spacing = 24):
  this_text_frame = createText(pos_x, pos_y, frame_width, frame_height)
  insertText(texts_list[0] + "\n", -1, this_text_frame)
  setFont(fonts_list[0], this_text_frame); setFontSize(font_sizes[0], this_text_frame)
  previous_line_length = getTextLength(this_text_frame)
  for idx in range(1,len(texts_list)):
    text_line = texts_list[idx]
    length_text_line = len(text_line)
    if idx < len(texts_list) - 1: insertText(text_line + "\n", -1, this_text_frame)
    else: insertText(text_line, -1, this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setFont(fonts_list[idx], this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setFontSize(font_sizes[idx], this_text_frame)
  setTextAlignment(ALIGN_CENTERED, this_text_frame); setTextColor(color, this_text_frame); setLineSpacing(line_spacing, this_text_frame)

def create_banner(banner_height, banner_width, origin_x, origin_y, banner_color, player_list):
  banner = createPolyLine([origin_x, origin_y, (origin_x+banner_width), origin_y, (origin_x+banner_width-banner_height/2), 
                          (origin_y+banner_height/2), (origin_x+banner_width), (origin_y+banner_height), 
                           origin_x, (origin_y+banner_height), (origin_x+banner_height/2), (origin_y+banner_height/2), origin_x, origin_y])
  setLineColor(banner_color, banner);
  vocales_acentos = ["Á", "É", "Í", "Ó", "Ú", "Ñ"]
  if any(x in unicode(player_list[0]).upper() for x in vocales_acentos): player_name_ypos = origin_y + banner_height/4 - 4
  else: player_name_ypos = origin_y + banner_height/4
  player_name = createText(origin_x, player_name_ypos, banner_width, banner_height)
  setText(unicode(player_list[0]).upper(), player_name)
  setTextColor(banner_color, player_name)
  setFont("News of the World Wide Italic", player_name); setFontSize(22, player_name)
  setTextAlignment(ALIGN_CENTERED, player_name)
  
  # text_frame(origin_x, origin_y + banner_height/4 + banner_height + 2, banner_width, banner_height, 
             # [player_list[2], "#" + player_list[3], "in " + player_list[5]], ["News of the World Wide Italic" for idx in range(3)], 
             # [22, 36, 24])
  
  player_stat = createText(origin_x, origin_y + banner_height/4 + banner_height + 2, banner_width, banner_height)
  setText(player_list[2], player_stat)
  setTextColor(banner_color, player_stat)
  setFont("News of the World Wide Italic", player_stat); setFontSize(22, player_stat)
  setTextAlignment(ALIGN_CENTERED, player_stat)
  
  player_rank = createText(origin_x, origin_y + 2 * banner_height/4 + 2 * banner_height - 5, banner_width, banner_height + 12)
  setText("#" + player_list[3], player_rank)
  setTextColor(banner_color, player_rank)
  setFont("News of the World Wide Italic", player_rank); setFontSize(36, player_rank)
  setTextAlignment(ALIGN_CENTERED, player_rank)
  
  player_division = createText(origin_x, origin_y + banner_height/4 + 3 * banner_height + 6, banner_width, banner_height)
  setText("in " + player_list[5], player_division)
  setTextColor(banner_color, player_division)
  setFont("News of the World Wide Italic", player_division); setFontSize(24, player_division)
  setTextAlignment(ALIGN_CENTERED, player_division)
  
  player_school = createText(origin_x, origin_y + banner_height/4 + 4 * banner_height + 12 + 33, banner_width, banner_height)
  setText(player_list[4].upper(), player_school)
  setTextColor(banner_color, player_school)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_school); setFontSize(10, player_school)
  setTextAlignment(ALIGN_CENTERED, player_school)
  
  player_div_ypos = getPosition(player_division)[1]
  player_school_ypos = getPosition(player_school)[1]
    
  logo_name = player_list[4].replace(" ", "_")
  # keep logo height fixed at 40 pt so we know it will always fit; compute logo width using the logo's aspect ratio
  logo_width = 40 / school_logos_dict[logo_name]
  school_logo = createImage(((origin_x - 36) + (306 - logo_width)/2), player_div_ypos + 12 + (player_school_ypos - player_div_ypos - 12)/2 - 20, logo_width, 40)
  loadImage("./School_Logos/" + player_list[4].replace(" ", "_") + ".gif", school_logo); setScaleImageToFrame(1, 1, school_logo)
  
  school_state = createText(origin_x, origin_y + banner_height/4 + 4 * banner_height + 12 + 44, banner_width, banner_height)
  setText(player_list[6], school_state)
  setTextColor(banner_color, school_state)
  setFont("Playball Regular", school_state); setFontSize(12, school_state)
  setTextAlignment(ALIGN_CENTERED, school_state)

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  
  # top_right_rect = createRect(306, 36, 306, 180)
  # setFillColor("NJCAA Gray", top_right_rect); setLineColor("NJCAA Gray", top_right_rect)
  # second_rect = createRect(0, 216, 306, 180)
  # setFillColor("NJCAA Gray", second_rect); setLineColor("NJCAA Gray", second_rect)
  # third_rect = createRect(306, 396, 306, 180)
  # setFillColor("NJCAA Gray", third_rect); setLineColor("NJCAA Gray", third_rect)
  # top_left_rect = createRect(0, 576, 306, 180)
  # setFillColor("NJCAA Gray", top_left_rect); setLineColor("NJCAA Gray", top_left_rect)
  
  num_players = len(players_list)
  if (num_players % 4) == 0: 
    num_pages = (num_players / 4) 
  else: 
    num_pages = (num_players / 4) + 1
  player_count = 0
  for page in range(num_pages):
    for idx in range(4):
      if (idx % 2) == 0:
        origin_x = 324; photo_x = 36; rect_x = 306
        if idx == 0:
          origin_y = 44; photo_y = 36; rect_y = 36
        else:
          origin_y = 404; photo_y = 396; rect_y = 396
      else:
        origin_x = 54; photo_x = 306; rect_x = 36
        if idx == 1:
          origin_y = 224; photo_y = 216; rect_y = 216
        else:
          origin_y = 584; photo_y = 576; rect_y = 576
        
      current_rect = createRect(rect_x, rect_y, 270, 180)
      setFillColor("White", current_rect); setLineColor("White", current_rect)
      
      current_player = players_list[player_count]
  
      player_photo = createImage(photo_x, photo_y, 270, 180)
      loadImage(current_player[1], player_photo); setScaleImageToFrame(1, 1, player_photo)
      
      photo_credit = "Photo: " + current_player[7].replace("\n", "")
      photo_credit_length = len(photo_credit)
      photo_credit_width = 4.0 * photo_credit_length + 2.0
      photo_credit_banner = createRect(photo_x + 270.0 - photo_credit_width, photo_y, photo_credit_width, 10)
      setFillColor("NJCAA Blue", photo_credit_banner); setLineColor("None", photo_credit_banner); setFillTransparency(0.70, photo_credit_banner)
        
        
      photo_credit_text = createText(photo_x + 270.0 - photo_credit_width, photo_y + 1.5, photo_credit_width, 12)
      setText(photo_credit, photo_credit_text)
      setTextColor("White", photo_credit_text); setFont("Asimov Print C", photo_credit_text); setFontSize(8, photo_credit_text)
      setTextAlignment(ALIGN_CENTERED, photo_credit_text)
  
      create_banner(banner_height = 24, banner_width = 234, origin_x = origin_x, origin_y = origin_y, 
                    banner_color = "NJCAA Blue", player_list = current_player)
      player_count += 1
      if player_count == num_players: break                    
  
    left_margin = createImage(0, 36, 36, 720)
    loadImage("./border_pattern.jpg", left_margin); setScaleImageToFrame(1, 1, left_margin)
    
    right_margin = createImage(576, 36, 36, 720)
    loadImage("./border_pattern.jpg", right_margin); setScaleImageToFrame(1, 1, right_margin)
    
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    # center_rect = createRect(0, 36, 612, 720)
    # setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    
    page_header = createText(36, 9, 540, 36)
    setText("Top 50", page_header)
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
      header_asterisk = createText(347, 9, 12, 36)
      setText("*", header_asterisk); setTextColor("White", header_asterisk); setFontSize(18, header_asterisk)
      
      footer_asterisk = createText(36, 758, 5, 34)
      setText("*", footer_asterisk); setTextColor("White", footer_asterisk); setFontSize(10, footer_asterisk)
      
      footnote_frame = createText(40, 758, 536, 35)
      footnote = "Players that were ranked nationally in the top 50 in their division in some statistical category. If a players was in the top 50 in two similar " \
                 "categories, e.g., digs and digs/set, she is featured as a leader in the one she ranked higgher." 
      setText(footnote, footnote_frame); setTextColor("White", footnote_frame); setFontSize(10, footnote_frame); setLineSpacing(11, footnote_frame)
      # break
    
    if player_count == num_players: break
    newPage(-1)
  