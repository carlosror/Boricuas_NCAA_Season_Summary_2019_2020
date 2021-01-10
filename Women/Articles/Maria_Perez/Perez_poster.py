#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (0, 0, 0, 0)

def text_frame(pos_x, pos_y, frame_width, frame_height, texts_list, fonts_list, font_sizes, colors, alignment = ALIGN_CENTERED, line_spacing = 24, scaling_h = 100):
  this_text_frame = createText(pos_x, pos_y, frame_width, frame_height)
  insertText(texts_list[0] + "\n", -1, this_text_frame)
  setFont(fonts_list[0], this_text_frame); setFontSize(font_sizes[0], this_text_frame); setTextColor(colors[0], this_text_frame)
  previous_line_length = getTextLength(this_text_frame)
  for idx in range(1,len(texts_list)):
    text_line = texts_list[idx]
    length_text_line = len(unicode(text_line))
    if idx < len(texts_list) - 1: insertText(text_line + "\n", -1, this_text_frame)
    else: insertText(text_line, -1, this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setFont(fonts_list[idx], this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setFontSize(font_sizes[idx], this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setTextColor(colors[idx], this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setTextAlignment(alignment, this_text_frame)
    previous_line_length += length_text_line + 1
  setTextAlignment(alignment, this_text_frame); setLineSpacing(line_spacing, this_text_frame)
  setTextScalingH(scaling_h, this_text_frame)

def draw_line(x1, y1, x2, y2, line_type = LINE_DASH, width = 1, color = "Map Blue"):
  this_line = createLine(x1, y1, x2, y2); setLineStyle(line_type, this_line); setLineColor(color, this_line)
  setLineWidth(width, this_line)
  
def insert_image(pos_x, pos_y, img_width, img_height, location):
  this_image = createImage(pos_x, pos_y, img_width, img_height); loadImage(location, this_image); setScaleImageToFrame(1, 1, this_image)

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
  defineColor("Maine_1", 212, 144, 6, 12)
  defineColor("Maine_2", 14, 21, 184, 1)
  
  center_rect = createRect(0, 0, 612, 792)
  setFillColor("White", center_rect); setLineColor("White", center_rect)
  top_rect = createRect(15, 15, 588, 124)
  setFillColor("Maine_1", top_rect); setLineColor("Maine_1", top_rect)
  
  insert_image(36, 47, 100, 100 * 330.0 / 487, "./../../School_Logos/Maine_Maritime_Academy.png")
  
  text_frame(15, 26, 588, 124, ["MARÍA PÉREZ", "COLLEGE CAREER RÉSUMÉ"], 
             ["Pink Sans 130" for idx in range(2)], [60, 30], colors = ["White" for idx in range(2)], line_spacing = 45, scaling_h = 120)
  
  poster_x = 15; poster_y = 153; poster_width = 294; poster_height = 294 * 1883.0 / 890.0
  insert_image(poster_x, poster_y, poster_width, poster_height, "Pérez_poster_1.jpg")
  
  photo_credit = "Photo: Tony Llerena"
  photo_credit_length = len(photo_credit)
  photo_credit_width = 95; photo_credit_height = 15
  photo_credit_banner = createRect(poster_x + poster_width - photo_credit_width, poster_y + poster_height - photo_credit_height, photo_credit_width, photo_credit_height)
  setFillColor("Maine_1", photo_credit_banner); setLineColor("None", photo_credit_banner); setFillTransparency(0.70, photo_credit_banner)
  
  text_frame(poster_x + poster_width - photo_credit_width + 3, poster_y + poster_height - photo_credit_height + 4, photo_credit_width, photo_credit_height, [photo_credit], ["Asimov Print C"], [10], colors = ["White"], alignment = ALIGN_LEFT)
  
  text_1_height = 80; text_1_ypos = 161.5; spacing = 34
  text_frame(330, text_1_ypos, 270, text_1_height, ["1,639", "career digs*"], ["Pink Sans 130", "Arial Regular"], 
             [60, 20], colors = ["Maine_1", "Black"], line_spacing = 30, alignment = ALIGN_LEFT)
  
  line_1_ypos = text_1_ypos + text_1_height + 12
  draw_line(330, line_1_ypos, 330 + 30, line_1_ypos, line_type = LINE_SOLID, color = "Black", width = 2)
  
  text_2_ypos = text_1_ypos + text_1_height + spacing
  text_frame(330, text_2_ypos, 270, text_1_height + 30, ["3x", "NAC Defensive \nPlayer of the Year**"], ["Pink Sans 130", "Arial Regular"], 
             [60, 20], colors = ["Maine_1", "Black"], line_spacing = 30, alignment = ALIGN_LEFT)
  
  line_2_ypos = text_2_ypos + text_1_height + 30 + 12
  draw_line(330, line_2_ypos, 330 + 30, line_2_ypos, line_type = LINE_SOLID, color = "Black", width = 2)
  
  text_3_ypos = text_2_ypos + text_1_height + 30 + spacing
  text_frame(330, text_3_ypos, 270, text_1_height + 30, ["3x", "NAC 1st Team \nAll-Conference***"], ["Pink Sans 130", "Arial Regular"], 
             [60, 20], colors = ["Maine_1", "Black"], line_spacing = 30, alignment = ALIGN_LEFT)
  
  line_3_ypos = text_3_ypos + text_1_height + 30 + 12
  draw_line(330, line_3_ypos, 330 + 30, line_3_ypos, line_type = LINE_SOLID, color = "Black", width = 2)
  
  text_4_ypos = text_3_ypos + text_1_height + 30 + spacing
  text_frame(330, text_4_ypos, 270, text_1_height + 30, ["3x", "NAC All-Tournament^"], ["Pink Sans 130", "Arial Regular"], 
             [60, 20], colors = ["Maine_1", "Black"], line_spacing = 30, alignment = ALIGN_LEFT)
  
  line_4_ypos = text_4_ypos + text_1_height + 12
  draw_line(330, line_4_ypos, 330 + 30, line_4_ypos, line_type = LINE_SOLID, color = "Black", width = 2)
  
  text_5_ypos = text_4_ypos + text_1_height + spacing
  text_frame(330, text_5_ypos, 270, text_1_height, ["1x", "Female Leader of the Year^^"], ["Pink Sans 130", "Arial Regular"], 
             [60, 20], colors = ["Maine_1", "Black"], line_spacing = 30, alignment = ALIGN_LEFT)
             
  footer = "*Maine Maritime Academy all-time leader **2016 - 2018 ***2017 - 2019 ^2016, 2017, 2019  ^^May 2020"
  text_frame(15, 780, 600, 20, [footer], ["Arial Regular"], [8], colors = ["Black"], line_spacing = 9, alignment = ALIGN_LEFT)