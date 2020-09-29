#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
import time
margins = (36, 36, 0, 0)

players_list = []
with open("NCAA_Division_2_players_2019_2020.csv") as f:
  next(f)
  for line in f:
    current_line_list = line.split(",")
    full_name = current_line_list[0].split()
    first_name = full_name[0]
    first_last_name = full_name[1]
    if (full_name[1] == "de" or full_name[1] == "La"): 
      image_filename = "./NCAA_DII_thumbs/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
      player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
    else:
      image_filename = "./NCAA_DII_thumbs/" + first_name + "_" + first_last_name + ".jpg"
      player_name = first_name + " " + first_last_name
    # cl_pos_ht = current_line_list[1] + " | " + current_line_list[2] + " | " + current_line_list[3]
    college = current_line_list[8]
    college_state = current_line_list[9]
    single_player_list = [image_filename, player_name, college, college_state]
    players_list.append(single_player_list)

# players_list = [(".\NCAA_DII_mugshots\Valeria_Aponte.jpg", "Valeria Aponte", "Jr. | DS/L | 5-7", "Guaynabo"), (".\NCAA_DII_mugshots\Naomi_Eckert.jpg", "Naomi Eckert", "Fr. | S | 5-8", "Toa Baja"),
                # (".\NCAA_DII_mugshots\Lyanne_Hernández.jpg", "Lyanne Hernández", "So. | OH | 5-8", "Patillas"), (".\NCAA_DII_mugshots\Claudia_González.jpg", "Claudia González", "So. | MB | 6-2", "Ponce"), 
                # (".\NCAA_DII_mugshots\Andrea_Serra.jpg", "Andrea Serra", "Jr. | OH | 5-10", "Toa Alta"), (".\NCAA_DII_mugshots\Michelle_Henwood.jpg", "Michelle Henwood", "Fr. | S | 5-9", "Guaynabo"), 
                # (".\NCAA_DII_mugshots\Itzel_Cruz.jpg", "Itzel Cruz", "Fr. | DS/L | 5-3", "San Juan"), (".\NCAA_DII_mugshots\Natalia_Quiñones.jpg", "Natalia Quiñones", "Sr. | MB | 6-0", "San Juan"),
                # (".\NCAA_DII_mugshots\Lara_Herrero.jpg", "Lara Herrero", "So. | OH | 5-8", "San Juan"), (".\NCAA_DII_mugshots\Ariana_Orcera.jpg", "Ariana Orcera", "Jr. | OH | 5-8", "Guaynabo"), 
                # (".\NCAA_DII_mugshots\Tammy_Reyes.jpg", "Tammy Reyes", "Jr. | S | 5-9", "Bayamón"), (".\NCAA_DII_mugshots\Liz_Ortiz.jpg", "Liz Ortiz", "Sr. | L | 5-8", "Coamo"), 
                # (".\NCAA_DII_mugshots\Valeria_Aldarondo.jpg", "Valeria Aldarondo", "So. | S | 5-8", "Isabela"), (".\NCAA_DII_mugshots\Gyanella_Vega.jpg", "Gyanella Vega", "Fr. | MB | 5-8", "Aguadilla"), 
                # (".\NCAA_DII_mugshots\Carolin_Santa.jpg", "Carolin Santa", "Jr. | OH | 5-9", "Arecibo"), (".\NCAA_DII_mugshots\Norian_Ceballos.jpg", "Norian Ceballos", "So. | MH | 5-11", "Loíza"), 
                # (".\NCAA_DII_mugshots\Isabel_Vega.jpg", "Isabel Vega", "So. | OH | 5-8", "Toa Alta"), (".\NCAA_DII_mugshots\Gabriela_Martínez.jpg", "Gabriela Martínez", "Sr. | DS | 5-2", "Vega Baja"), 
                # (".\NCAA_DII_mugshots\Natalia_Cruz.jpg", "Natalia Cruz", "Sr. | DS/L | 5-9", "San Juan"), (".\NCAA_DII_mugshots\Claudia_Rivera.jpg", "Claudia Rivera", "So. | L | 5-3", "Gurabo"), 
                # (".\NCAA_DII_mugshots\Nicole_Domínguez.jpg", "Nicole Domínguez", "Sr. | L | 5-8", "Manatí"), (".\NCAA_DII_mugshots\Fabiola_Rosado.jpg", "Fabiola Rosado", "Sr. | DS | 5-1", "San Juan"), 
                # (".\NCAA_DII_mugshots\Alondra_Rodríguez.jpg", "Alondra Rodríguez", "Jr. | L | 5-4", "Bayamón"), (".\NCAA_DII_mugshots\Sheila_Villagrasa.jpg", "Sheila Villagrasa", "Sr. | S | 5-9", "San Juan"), 
                # (".\NCAA_DII_mugshots\Anixa_Rosa.jpg", "Anixa Rosa", "Fr. | OH | 5-8", "San Lorenzo"), (".\NCAA_DII_mugshots\Alondra_Díaz.jpg", "Alondra Díaz", "So. | DS/L | 5-4", "Toa Alta"), 
                # (".\NCAA_DII_mugshots\Junelly_Marrero.jpg", "Junelly Marrero", "Jr. | DS/L | 5-4", "Cataño"), (".\NCAA_DII_mugshots\Alejandra_Leal.jpg", "Alejandra Leal", "Jr. | DS/L | 5-4", "Gurabo"), 
                # (".\NCAA_DII_mugshots\Tanializ_Rivera.jpg", "Tanializ Rivera", "Fr. | MB | 5-11", "Carolina"),(".\NCAA_DII_mugshots\Lydimar_Soto.jpg", "Lydimar Soto", "Fr. | DS | 5-5", "Trujillo Alto"), 
                # (".\NCAA_DII_mugshots\Alana_Rousset.jpg", "Alana Rousset", "Sr. | DS/S | 5-2", "Canóvanas"), (".\NCAA_DII_mugshots\Militza_de_Hostos.jpg", "Militza de Hostos", "So. | RSH | 5-7", "Bayamón"), 
                # (".\NCAA_DII_mugshots\Nilka_Rivera.jpg", "Nilka Rivera", "So. | OH | 5-11", "Bayamón"), (".\NCAA_DII_mugshots\Camila_Rabassa.jpg", "Camila Rabassa", "Sr. | OH | 6-0", "Juana Díaz"), 
                # (".\NCAA_DII_mugshots\Paula_Céspedes.jpg", "Paula Céspedes", "Jr. | DS/L | 5-0", "Carolina"), (".\NCAA_DII_mugshots\Talía_González.jpg", "Talía González", "Fr. | OH | 6-0", "Florida"), 
                # (".\NCAA_DII_mugshots\Vanelix_Merced.jpg", "Vanelix Merced", "Sr. | DS/L | 5-4", "Guaynabo"), (".\NCAA_DII_mugshots\Nahomie_Alejandro.jpg", "Nahomie Alejandro", "Fr. | MB/RSH | 5-10", "Bayamón"),
                # (".\NCAA_DII_mugshots\Mainerys_Muñoz.jpg", "Mainerys Muñoz", "Fr. | DS/L | 5-7", "Bayamón"), (".\NCAA_DII_mugshots\Ariana_Rosario.jpg", "Ariana Rosario", "Sr. | OH/RSH | 5-9", "Guaynabo"), 
                # (".\NCAA_DII_mugshots\Bianca_Díaz.jpg", "Bianca Díaz", "Fr. | DS/L | 5-7", "Humacao"),]
if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("White", center_rect); setLineColor("White", center_rect)
  
  pic_x_coord = 36; pic_y_coord = 42
  num_players = len(players_list)
  thumb_w = 26.2
  thumb_h = 36
  num_rows = 20; num_cols = 2
  row_sum_start = 0
  if (num_players % 40) == 0: 
    num_pages = (num_players / 40) 
  else: 
    num_pages = (num_players / 40) + 1
  player_count = 0
  players_list_size = len(players_list)
  
  for page in range(num_pages):
    for col in range(num_cols):
      for row in range(num_rows):
        if ((row + 1) % 2) == 0:
          gray_row = createRect((270 * col + 36), (36 + row * 36), 276, 36)
          setFillColor("NJCAA Gray", gray_row); setLineColor("NJCAA Gray", gray_row)
        player_count += 1
    
    if player_count == players_list_size: break
    newPage(-1)
  
  gotoPage(1)
  player_count = 0
  for page in range(num_pages):
    for col in range(num_cols):
      for row in range(num_rows):
        # if ((row + 1) % 2) == 0:
          # gray_row = createRect((270 * col + 36), (36 + row * 36), 276, 36)
          # setFillColor("NJCAA Gray", gray_row); setLineColor("NJCAA Gray", gray_row)
        
        current_player = players_list[player_count]
        
        thumb_x = 270 * col + 36 + 4
        thumb_y = 36 + row * 36
        player_thumb = createImage(thumb_x,thumb_y, thumb_w, thumb_h)
        loadImage(current_player[0], player_thumb); setScaleImageToFrame(1, 1, player_thumb)
        
        thumb_name_x = thumb_x + thumb_w + 4
        thumb_name_w = 60
        thumb_name_frame = createText(thumb_name_x, thumb_y + 8, 236, 22)
        player_name_first = current_player[1].split(" ")[0]
        player_name_last = current_player[1].split(" ")[1]
        player_college_first = current_player[2].split(" ")[0] + current_player[2].split(" ")[1]
        player_college_last = " ".join(current_player[2].split(" ")[2:])
        player_first = player_name_first + "             " + player_college_first + "             " + current_player[3] + "\n"
        player_last = player_name_last + "             " + player_college_last
        setText(player_first + player_last, thumb_name_frame)
        setFont("Asimov Print C", thumb_name_frame); setFontSize(8.5, thumb_name_frame)
        setTextColor("NJCAA Blue", thumb_name_frame); setLineSpacing(12, thumb_name_frame)
        
        # thumb_college_x = thumb_name_x + thumb_name_w
        # thumb_college_w = 110
        # player_college_array = current_player[2].split(" ")
        # if len(player_college_array) > 2: player_college = " ".join(player_college_array[0:2]) + "\n" + " ".join(player_college_array[2:])
        # else: player_college = " ".join(player_college_array[0:1]) + "\n" + " ".join(player_college_array[1:])
        # thumb_college_frame = createText(thumb_college_x, thumb_y + 8, thumb_college_w, 22)
        # setText(player_college, thumb_college_frame)
        # setFont("Asimov Print C", thumb_college_frame); setFontSize(8.5, thumb_college_frame)
        # setTextColor("NJCAA Blue", thumb_college_frame); setLineSpacing(12, thumb_college_frame)
        
        # thumb_state_x = thumb_college_x + thumb_college_w
        # thumb_state_w = 66
        # thumb_state_frame = createText(thumb_state_x, thumb_y + 8 + 8, thumb_state_w, 22)
        # setText(current_player[3], thumb_state_frame)
        # setFont("Asimov Print C", thumb_state_frame); setFontSize(8.5, thumb_state_frame)
        # setTextColor("NJCAA Blue", thumb_state_frame); setLineSpacing(12, thumb_state_frame)
        
        player_count += 1
        if player_count == players_list_size: break
      if player_count == players_list_size: break
    
    middle_line = createLine((612 - 72) / 2 + 36, 36, (612 - 72) / 2 + 36, 756)
    setLineColor("NJCAA Blue", middle_line)
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    
    left_margin = createImage(0, 36, 36, 720)
    loadImage("./border_pattern.jpg", left_margin); setScaleImageToFrame(1, 1, left_margin)
    right_margin = createImage(576, 36, 36, 720)
    loadImage("./border_pattern.jpg", right_margin); setScaleImageToFrame(1, 1, right_margin)
    
    if player_count == players_list_size: break
    
    gotoPage(page + 2)
        
        # name_pos_x = 270 * col + 36 + 4 + thumb_w + 3.8
        # name_pox_y = 36 + row * 36 + 8
        # player_name = createText(name_pos_x, name_pox_y, 60, 22)
        