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
                (".\NCAA_DI_mugshots\Laura_Rojas.jpg", "Laura Rojas", "Sr. | DS/L | 5-4", ""), (".\NCAA_DI_mugshots\Natalia_Rivera.jpg", "Natalia Rivera", "Sr. | L | 5-4", "Cayey"), 
                (".\NCAA_DI_mugshots\Cristina_Robles.jpg", "Cristina Robles", "Jr. |  DS/L | 5-2", "Bayamón"), (".\NCAA_DI_mugshots\Kizzy_Rodríguez.jpg", "Kizzy Rodríguez", "Jr. |  L | 5-4", "Luquillo"),
                (".\NCAA_DI_mugshots\Ivana_Marrero.jpg", "Ivana Marrero", "Fr. | S | 5-7", "Dorado"), (".\NCAA_DI_mugshots\Génesis_Soto.jpg", "Génesis Soto", "Jr. |  DS/L | 5-2", "Trujillo Alto"), 
                (".\NCAA_DI_mugshots\Kelly_Negrón.jpg", "Kelly Negrón", "Fr. | S | 5-7", "Arecibo"), (".\NCAA_DI_mugshots\Alejandra_Rodríguez.jpg", "Alejandra Rodríguez", "Sr. | L | 5-4", "Toa Alta"), 
                (".\NCAA_DI_mugshots\Angeleyshka_Curbelo.jpg", "Angeleyshka Curbelo", "So. | OH | 6-0", "Carolina"), (".\NCAA_DI_mugshots\Stephanie_Rivera.jpg", "Stephanie Rivera", "So. | MH | 5-11", "Guayama"), 
                (".\NCAA_DI_mugshots\Alanis_Alvarado.jpg", "Alanis Alvarado", "So. | OH | 5-11", "Bayamón"), (".\NCAA_DI_mugshots\Yaidelis_López.jpg", "Yaidelis López", "Jr. | DS/L | 5-0", "Caguas"),
                (".\NCAA_DI_mugshots\Karla_Seda.jpg", "Karla Seda", "Jr. | L | 5-2", "Toa Baja"), (".\NCAA_DI_mugshots\Wildalys_Soto.jpg", "Wildalys Soto", "Jr. | S | 5-10", "Patillas"), 
                (".\NCAA_DI_mugshots\Nashally_Eleutiza.jpg", "Nashally Eleutiza", "Jr. | DS | 5-8", ""), (".\NCAA_DI_mugshots\Paulina_Pérez.jpg", "Paulina Pérez", "So. | OH | 6-0", "Guánica"), 
                (".\NCAA_DI_mugshots\Fabiola_Rivas.jpg", "Fabiola Rivas", "Sr. | DS | 5-5", "San Juan"), (".\NCAA_DI_mugshots\Jaylibeth_García.jpg", "Jaylibeth García", "Fr. | MB | 6-1", "Toa Baja"), 
                (".\NCAA_DI_mugshots\Alejandra_Pérez.jpg", "Alejandra Pérez", "Jr. | OH | 5-8", "Ponce"), (".\NCAA_DI_mugshots\Rocío_Moro.jpg", "Rocío Moro", "So. | DS/L | 5-5", "San Juan"), 
                (".\NCAA_DI_mugshots\Solimar_Cestero.jpg", "Solimar Cestero", "So. | OH | 6-0", "Toa Baja"), (".\NCAA_DI_mugshots\Charyari_Ramos.jpg", "Charyari Ramos", "So. | OH/S | 5-11", "Ponce"), 
                (".\NCAA_DI_mugshots\Angelie_Rosario.jpg", "Angelie Rosario", "Fr. | DS | 5-7", "Bayamón"), (".\NCAA_DI_mugshots\Mariana_Trujillo.jpg", "Mariana Trujillo", "Fr. | S | 5-9", "Guayanilla"), (".\NCAA_DI_mugshots\Alahna_Díaz.jpg", "Alahna Díaz", "Sr. | L | 5-4", "Carolina"), 
                (".\NCAA_DI_mugshots\Katerina_Rocafort.jpg", "Katerina Rocafort", "Sr. | S | 5-8", "San Juan"), (".\NCAA_DI_mugshots\Cecilia_Rocafort.jpg", "Cecilia Rocafort", "Fr. | S | 5-8", "San Juan"), 
                (".\NCAA_DI_mugshots\Sharlissa_De_Jesús.jpg", "Sharlissa de Jesús", "Jr. | OH | 5-9", "Guayama"), (".\NCAA_DI_mugshots\Paola_Santiago.jpg", "Paola Santiago", "So. | OH | 5-9", "San Juan")]
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
    page_header = createText(36, 10, 540, 36)
    setText("NCAA Division I Players Snapshots", page_header)
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
        if player_count == num_players: exit()
    
        pic_x_coord += 111
        row_sum -= row - 1
      pic_y_coord += 180
      pic_x_coord = 36
      #row_sum += 4
    newPage(-1)
    top_rect = createRect(0, 0, 612, 36)
    setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
    bottom_rect = createRect(0, 756, 612, 36)
    setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
    center_rect = createRect(0, 36, 612, 720)
    setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    pic_x_coord = 36; pic_y_coord = 42