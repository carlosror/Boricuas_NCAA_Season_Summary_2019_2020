#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (0, 0, 0, 0)

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
  setTextAlignment(alignment, this_text_frame); setTextColor(color, this_text_frame); setLineSpacing(line_spacing, this_text_frame)

def draw_line(x1, y1, x2, y2, line_type = LINE_DASH, width = 1, color = "Map Blue"):
  this_line = createLine(x1, y1, x2, y2); setLineStyle(line_type, this_line); setLineColor(color, this_line)
  setLineWidth(width, this_line)
  
def insert_image(pos_x, pos_y, img_width, img_height, location):
  this_image = createImage(pos_x, pos_y, img_width, img_height); loadImage(location, this_image); setScaleImageToFrame(1, 1, this_image)

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("AIC Yellow", 8, 30, 231, 3)
  
  # Top and bottom banners
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("AIC Yellow", top_rect); setLineColor("AIC Yellow", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("AIC Yellow", bottom_rect); setLineColor("AIC Yellow", bottom_rect)
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
  
  # Title and years
  text_frame(36, 9, 540, 36, ["Andrea Serra and Naomi Eckert"], ["OLD SPORT 02 ATHLETIC NCV Regular"], [24], color = "Black")  
  text_frame(0, 6.7, 36, 36, ["2019", "-", "2020"], ["OLD SPORT 02 ATHLETIC NCV Regular" for idx in range(3)], [11,11, 11], color = "Black", line_spacing = 7)
  text_frame(576, 6.7, 36, 36, ["2019", "-", "2020"], ["OLD SPORT 02 ATHLETIC NCV Regular" for idx in range(3)], [11,11, 11], color = "Black", line_spacing = 7)
  
  # Serra image
  insert_image(36, 50, 540, 360, "Andrea_Serra_Banner.jpg")
  
  # Background for plots, etc
  center_rect = createRect(36, 50 + 360, 540, 336)
  setFillColor("White", center_rect); setLineColor("White", center_rect)
  
  # Image title
  text_frame(36, 420, 540, 36, ["Andrea Serra's Banner Year"], ["OLD SPORT 01 COLLEGE NCV Regular"], [32], color = "Black")
  
  # Lines
  line_xpos = 57; line_ypos = 455; line_width = 492; line_sep = 100
  draw_line(line_xpos, line_ypos, line_xpos + line_width, line_ypos, line_type = LINE_SOLID, width = 2, color = "Black")
  draw_line(line_xpos, line_ypos + line_sep, line_xpos + line_width, line_ypos + line_sep, line_type = LINE_SOLID, width = 2, color = "Black")
  
  line_height = 36.0
  draw_line(line_xpos + line_width / 3.0, line_ypos + (line_sep - line_height) / 2.0, line_xpos + line_width / 3.0, line_ypos + (line_sep - line_height) / 2.0 + line_height, line_type = LINE_SOLID, width = 2, color = "Black")
  draw_line(line_xpos + 2 * (line_width / 3.0), line_ypos + (line_sep - line_height) / 2.0, line_xpos + 2 * (line_width / 3.0), line_ypos + (line_sep - line_height) / 2.0 + line_height, line_type = LINE_SOLID, width = 2, color = "Black")
  
  # Large stats
  text_height = 64
  text_frame(line_xpos, line_ypos + (line_sep - text_height) / 2.0 + 3, line_width / 3.0, text_height, ["532", "kills"], ["Pink Sans 130", "Pink Sans 130"], [50, 20], color = "Black")
  text_frame(line_xpos + (line_width / 3.0), line_ypos + (line_sep - text_height) / 2.0 + 3, line_width / 3.0, text_height, ["414", "digs"], ["Pink Sans 130", "Pink Sans 130"], [50, 20], color = "Black")
  text_frame(line_xpos + 2 * (line_width / 3.0), line_ypos + (line_sep - text_height) / 2.0 + 3, line_width / 3.0, text_height, ["55", "aces"], ["Pink Sans 130", "Pink Sans 130"], [50, 20], color = "Black")
  
  # Large asterisks
  text_frame(170, 473, 17, 18, ["*"], ["Arial Regular"], [18], color = "Black", alignment = ALIGN_LEFT)
  text_frame(170 + line_width / 3.0, 473, 17, 18, ["*"], ["Arial Regular"], [18], color = "Black", alignment = ALIGN_LEFT)
  
  # Second header
  text_frame(36, line_ypos + 115, 540, 36, ["Single-match highs in 2018 and 2019"], ["Arial Regular"], [24], color = "Black")
  
  #Plots
  plot_width = 510
  insert_image(line_xpos - 6, line_ypos + 140, plot_width / 3.0, (plot_width / 3.0) * (1581 / 2100.0), "serra_kills.png")
  insert_image(line_xpos  - 6+ (plot_width / 3.0), line_ypos + 140, plot_width / 3.0, (plot_width / 3.0) * (1581 / 2100.0), "serra_digs.png")
  insert_image(line_xpos - 6 + 2 * (plot_width / 3.0), line_ypos + 140, plot_width / 3.0, (plot_width / 3.0) * (1581 / 2100.0), "serra_aces.png")
  
  # Small asterisk
  text_frame(58, 725, 11, 18, ["*"], ["Arial Regular"], [12], color = "Black")
  text_frame(66, 727, plot_width, 18, ["1 of only 2 players in NCAA DII with 500+ kills and 400+ digs"], 
             ["Arial Regular"], [8], color = "Black", alignment = ALIGN_LEFT)