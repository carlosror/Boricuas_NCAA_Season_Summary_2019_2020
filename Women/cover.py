#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (0, 0, 0, 0)




if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
  
  bg_rect = createRect(0, 0, 612, 792)
  setFillColor("NJCAA Blue", bg_rect); setLineColor("NJCAA Blue", bg_rect)
  
  row_count = 0
  for row in ["Digging", "Setting", "Killing", "Celebrating", "Serving", "Beach"]:
    for col in range(6):
      photo_width = 102; photo_height = 102
      photo_x = col * photo_width
      if row_count < 4: photo_y = row_count * photo_height 
      else: photo_y = row_count * photo_height + 180
      photo = createImage(photo_x, photo_y, photo_width, photo_height)
      loadImage("./Cover/" + row + "/" + str(col + 1) + ".jpg", photo); setScaleImageToFrame(1, 1, photo)
    
    row_count += 1
  
  title_xpos = 36; title_ypos = 4 * photo_height + 25; title_width = 540; title_height = 100
  title = createText(title_xpos, title_ypos, title_width, title_height)
  insertText("Puerto Rico Women's College Volleyball", -1, title)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", title); setFontSize(48, title); setTextColor("White", title)
  setTextAlignment(ALIGN_CENTERED, title); setLineSpacing(50, title)
  subtitle = createText(title_xpos, title_ypos + title_height + 10, title_width, title_height / 1.5)
  insertText("Academic Year 2019-2020", -1, subtitle)
  setFont("Playball Regular", subtitle); setFontSize(35, subtitle); setTextColor("White", subtitle)
  setTextAlignment(ALIGN_CENTERED, subtitle)