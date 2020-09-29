#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)
players_list = [(".\NCAA_DI_mugshots\Ariana_Pagán.jpg", "Ariana Pagán", "Fr. | OH | 5-10", "Isabela"), (".\NCAA_DI_mugshots\Yelianiz_Torres.jpg", "Yelianiz Torres", "Fr. | OH | 5-7", "Vega Baja"),
                (".\NCAA_DI_mugshots\Amanda_Rullán.jpg", "Amanda Rullán", "Jr. | OH | 5-10", "Bayamón"), (".\NCAA_DI_mugshots\Paula_Cerame.jpg", "Paula Cerame", "Jr. | DS/L | 5-7", "San Juan"),
                (".\NCAA_DI_mugshots\Andrea_Fuentes.jpg", "Andrea Fuentes", "So. | S | 5-9", "San Juan"), (".\NCAA_DI_mugshots\Dariana_Hollingsworth.jpg", "Dariana Hollingsworth", "Jr. | OH/RSH | 6-1", "San Juan"), 
                (".\NCAA_DI_mugshots\Leandra_Mangual.jpg", "Leandra Mangual", "Fr. | OH | 6-0", "Río Grande"), (".\NCAA_DI_mugshots\Camilla_Covas.jpg", "Camilla Covas", "Fr. | DS | 5-6", "San Juan"), 
                (".\NCAA_DI_mugshots\Lina_Bernier.jpg", "Lina Bernier", "Sr. | DS/L | 5-11", "San Juan"), (".\NCAA_DI_mugshots\Fabiola_Plaza.jpg", "Fabiola Plaza", "Sr. | DS/S | 5-6", "Ponce"), 
                (".\NCAA_DI_mugshots\Gina_Rivera.jpg", "Gina Rivera", "So. | L | 5-6", "Lajas"), (".\NCAA_DI_mugshots\Kariely_Santana.jpg", "Kariely Santana", "Jr. | OH | 5-10", "Caguas"), 
                (".\NCAA_DI_mugshots\Sofía_García.jpg", "Sofía García", "Fr. | S | 5-10", "Manatí"), (".\NCAA_DI_mugshots\Alondrah_Santana.jpg", "Alondrah Santana", "Fr. | MB | 6-1", "Toa Baja"), 
                (".\NCAA_DI_mugshots\Jennevy_Santos.jpg", "Jennevy Santos", "Jr. | L | 5-4", "Bayamón"), (".\NCAA_DI_mugshots\Ashley_Román.jpg", "Ashley Román", "Fr. | DS/L | 5-5", "Isabela"), 
                (".\NCAA_DI_mugshots\Salma_González.jpg", "Salma González", "Jr. | S/OH | 5-8", "Isabela"), (".\NCAA_DI_mugshots\Jasmal_Cruz.jpg", "Jasmal Cruz", "Fr. | L | 5-7", "Trujillo Alto"), 
                (".\NCAA_DI_mugshots\Anadys_Valentín.jpg", "Anadys Valentín", "Fr. | OH | 5-11", "Vega Baja"), (".\NCAA_DI_mugshots\Andrea_Laboy.jpg", "Andrea Laboy", "So. | L | 5-5", "Coamo"), 
                (".\NCAA_DI_mugshots\Yamelis_Mojica.jpg", "Yamelis Mojica", "Fr. | OH/MB | 6-2", "Bayamón"), (".\NCAA_DI_mugshots\Valeria_Vázquez.jpg", "Valeria Vázquez", "Fr. | OH | 6-1", "Manatí"), 
                (".\NCAA_DI_mugshots\Melanie_Feliciano.jpg", "Melanie Feliciano", "Fr. | OH | 5-11", "Ponce"), (".\NCAA_DI_mugshots\Laura_Ruiz.jpg", "Laura Ruiz", "Fr. | DS/L | 5-7", "Cayey"), 
                (".\NCAA_DI_mugshots\Cecilia_Thon.jpg", "Cecilia Thon", "So. | S | 5-7", "San Juan"), (".\NCAA_DI_mugshots\Alondra_Vázquez.jpg", "Alondra Vázquez", "So. | OH | 5-11", "Toa Alta"), 
                (".\NCAA_DI_mugshots\Laura_Rojas.jpg", "Laura Rojas", "Sr. | DS/L | 5-4", "")]
if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):
  top_line = createLine(0, 36, 612, 36)
  bottom_line = createLine(0, 756, 612, 756)
  # image_frame_1 = createImage(36, 42, 96, 128)
  # loadImage("Gina_Rivera_Ortiz.jpg", image_frame_1)
  # setScaleImageToFrame(1, 1, image_frame_1)
  pic_x_coord = 36; pic_y_coord = 42
  num_players = len(players_list)
  mugshot_w = 96
  mugshot_h = 128
  num_rows = 4; num_cols = 5
  row_sum_start = 0
  num_pages = 2
  for page in range(1, num_pages + 1):
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
        setTextAlignment(ALIGN_CENTERED, mugshot_text_name)
    
        player_class_text_height = 11
        mugshot_text_class = createText(pic_x_coord, pic_y_coord + mugshot_h + 5 + player_name_text_height, mugshot_w, player_class_text_height)
        setText(players_list[idx][2] + "\n", mugshot_text_class)
        setFont("Asimov Print C", mugshot_text_class); setFontSize(player_class_text_height - 2, mugshot_text_class)
        setTextAlignment(ALIGN_CENTERED, mugshot_text_class)
    
        player_hometown_text_height = 13
        mugshot_text_hometown = createText(pic_x_coord, pic_y_coord + mugshot_h + 5 + player_name_text_height + player_class_text_height , mugshot_w, player_hometown_text_height)
        setText(players_list[idx][3] + "\n", mugshot_text_hometown)
        setFont("Playball Regular", mugshot_text_hometown); setFontSize(player_hometown_text_height - 2, mugshot_text_hometown)
        setTextAlignment(ALIGN_CENTERED, mugshot_text_hometown)
    
        pic_x_coord += 111
        row_sum -= row - 1
      pic_y_coord += 180
      pic_x_coord = 36
      #row_sum += 4
    newPage(-1)
    top_line = createLine(0, 36, 612, 36)
    bottom_line = createLine(0, 756, 612, 756)
    pic_x_coord = 36; pic_y_coord = 42