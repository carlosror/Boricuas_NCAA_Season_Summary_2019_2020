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
      image_filename = "./NCAA_DII_mugshots_2/" + first_name + "_" + full_name[1] + "_" + full_name[2] + ".jpg"
      player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
    else:
      image_filename = "./NCAA_DII_mugshots_2/" + first_name + "_" + first_last_name + ".jpg"
      player_name = first_name + " " + first_last_name
    cl_pos_ht = current_line_list[1] + " | " + current_line_list[2] + " | " + current_line_list[3]
    hometown = current_line_list[6]
    single_player_list = [image_filename, player_name, cl_pos_ht, hometown]
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
  
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
  
  pic_x_coord = 36; pic_y_coord = 42
  num_players = len(players_list)
  mugshot_w = 96
  mugshot_h = 128
  num_rows = 4; num_cols = 5
  row_sum_start = 0
  if (num_players % 20) == 0: 
    num_pages = (num_players / 20) 
  else: 
    num_pages = (num_players / 20) + 1
  player_count = 0
  for page in range(1, num_pages + 1):
    start = time.time()
    page_header = createText(36, 9, 540, 36)
    setText("NCAA Division II Players Snapshots", page_header)
    setTextColor("White", page_header)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(24, page_header)
    setTextAlignment(ALIGN_CENTERED, page_header)
    for row in range(1, num_rows + 1):
      row_sum = 4 * (row - 1) 
      for col in range(1, num_cols + 1):
        mugshot = createImage(pic_x_coord, pic_y_coord, mugshot_w, mugshot_h)
        idx = row * col + row_sum - 1 + 20 * (page - 1)
        loadImage(players_list[idx][0], mugshot)
        setScaleImageToFrame(1, 1, mugshot)
    
        player_name_text_height = 11
        mugshot_text_name = createText(pic_x_coord, pic_y_coord + mugshot_h + 5, mugshot_w, player_name_text_height)
        setText(players_list[idx][1] + "\n", mugshot_text_name)
        setFont("Asimov Print C", mugshot_text_name); setFontSize(player_name_text_height - 2, mugshot_text_name)
        setTextColor("NJCAA Blue", mugshot_text_name)
        setTextAlignment(ALIGN_CENTERED, mugshot_text_name)
    
        player_class_text_height = 11
        mugshot_text_class = createText(pic_x_coord, pic_y_coord + mugshot_h + 5 + player_name_text_height, mugshot_w, player_class_text_height)
        setText(players_list[idx][2] + "\n", mugshot_text_class)
        setFont("Asimov Print C", mugshot_text_class); setFontSize(player_class_text_height - 2, mugshot_text_class)
        setTextColor("NJCAA Blue", mugshot_text_class)
        setTextAlignment(ALIGN_CENTERED, mugshot_text_class)
    
        player_hometown_text_height = 13
        mugshot_text_hometown = createText(pic_x_coord, pic_y_coord + mugshot_h + 5 + player_name_text_height + player_class_text_height , mugshot_w, player_hometown_text_height)
        setText(players_list[idx][3] + "\n", mugshot_text_hometown)
        setFont("Playball Regular", mugshot_text_hometown); setFontSize(player_hometown_text_height - 2, mugshot_text_hometown)
        setTextColor("NJCAA Blue", mugshot_text_hometown)
        setTextAlignment(ALIGN_CENTERED, mugshot_text_hometown)
        
        player_count += 1
        if player_count == num_players: 
          end = time.time()
          page_time = str(end - start)
          page_debug = createText(576, 756, 36, 36)
          setText(page_time, page_debug)
          exit()
    
        pic_x_coord += 111
        row_sum -= row - 1
      pic_y_coord += 180
      pic_x_coord = 36
      #row_sum += 4
    end = time.time()
    page_time = str(end - start)
    page_debug = createText(576, 756, 36, 36)
    setText(page_time, page_debug)
    newPage(-1)
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    center_rect = createRect(0, 36, 612, 720)
    setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    pic_x_coord = 36; pic_y_coord = 42