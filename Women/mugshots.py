#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)
players_list = [("Ellisangi_Matos_Torres.jpeg", "Ellisangi Matos", "Sr. | S | 5-3", "Río Grande"), ("Gina_Rivera_Ortiz.jpg", "Gina Rivera", "So. | L | 5-6", "Lajas"),
                ("Patricia_Martínez.png", "Patricia Martínez", "Jr. | OH | 5-10", "Guaynabo"), ("Gina_Rivera_Ortiz.jpg", "Gina Rivera", "So. | L | 5-6", "Lajas"),
                ("Gina_Rivera_Ortiz.jpg", "Gina Rivera", "So. | L | 5-6", "Lajas")]
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
  for idx in range(5):
    mugshot = createImage(pic_x_coord, pic_y_coord, mugshot_w, mugshot_h)
    loadImage(players_list[idx][0], mugshot)
    setScaleImageToFrame(1, 1, mugshot)
    
    player_name_text_height = 14
    mugshot_text_name = createText(pic_x_coord, pic_y_coord + mugshot_h + 5, mugshot_w, player_name_text_height)
    setText(players_list[idx][1] + "\n", mugshot_text_name)
    setFont("Asimov Print C", mugshot_text_name); setFontSize(player_name_text_height - 2, mugshot_text_name)
    setTextAlignment(ALIGN_CENTERED, mugshot_text_name)
    
    player_class_text_height = 11
    mugshot_text_class = createText(pic_x_coord, pic_y_coord + mugshot_h + 5 + player_name_text_height, mugshot_w, player_class_text_height)
    setText(players_list[idx][2] + "\n", mugshot_text_class)
    setFont("Asimov Print C", mugshot_text_class); setFontSize(player_class_text_height - 2, mugshot_text_class)
    setTextAlignment(ALIGN_CENTERED, mugshot_text_class)
    
    player_hometown_text_height = 14
    mugshot_text_hometown = createText(pic_x_coord, pic_y_coord + mugshot_h + 5 + player_name_text_height + player_class_text_height , mugshot_w, player_hometown_text_height)
    setText(players_list[idx][3] + "\n", mugshot_text_hometown)
    setFont("Playball Regular", mugshot_text_hometown); setFontSize(player_hometown_text_height - 2, mugshot_text_hometown)
    setTextAlignment(ALIGN_CENTERED, mugshot_text_hometown)
    
    pic_x_coord += 111