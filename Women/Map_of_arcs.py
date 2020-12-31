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
  setTextAlignment(ALIGN_CENTERED, this_text_frame); setTextColor(color, this_text_frame); setLineSpacing(line_spacing, this_text_frame)

def draw_line(x1, y1, x2, y2, line_type = LINE_DASH, color = "Map Blue", width = 1.0):
  this_line = createLine(x1, y1, x2, y2); setLineStyle(line_type, this_line); setLineColor(color, this_line)
  setLineWidth(width, this_line)
  
def insert_image(pos_x, pos_y, img_width, img_height, location, line_color = "NJCAA Blue"):
  this_image = createImage(pos_x, pos_y, img_width, img_height); loadImage(location, this_image); setScaleImageToFrame(1, 1, this_image)
  setLineColor(line_color, this_image)

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
  defineColor("Map Blue", 113, 65, 5, 4)
  
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
  
  text_frame(36, 9, 540, 36, ["From the island to the mainland"], ["OLD SPORT 02 ATHLETIC NCV Regular"], [24], color = "White")  
  text_frame(0, 6.7, 36, 36, ["2019", "-", "2020"], ["OLD SPORT 02 ATHLETIC NCV Regular" for idx in range(3)], [11,11, 11], color = "White", line_spacing = 7)
  text_frame(576, 6.7, 36, 36, ["2019", "-", "2020"], ["OLD SPORT 02 ATHLETIC NCV Regular" for idx in range(3)], [11,11, 11], color = "White", line_spacing = 7)
    
  # Map of arcs
  insert_image(36, 40, 540, 406, "./../Maps/arcs_map.png")
  
  # First row
  text_width_1 = 116; text_width_2 = 92; text_width_3 = 98; text_width_4 = 62; text_height = 87
  blank_space = (540 - (text_width_1 + text_width_2 + text_width_3 + text_width_4)) / 5.0
  text_frame(36 + blank_space, 482, text_width_1, text_height, ["275", "student athletes"], ["Pink Sans 130", "Pink Sans 130"], [70, 20])
  text_frame(36 + 2 * blank_space + text_width_1, 482, text_width_2, text_height, ["158", "institutions"], ["Pink Sans 130", "Pink Sans 130"], [70, 20])
  text_frame(36 + 3 * blank_space + text_width_1 + text_width_2, 482, text_width_3, text_height, ["58", "municipalities"], ["Pink Sans 130", "Pink Sans 130"], [70, 20])
  text_frame(36 + 4 * blank_space + text_width_1 + text_width_2 + text_width_3, 482, text_width_4, text_height, ["33", "states"], ["Pink Sans 130", "Pink Sans 130"], [70, 20])
  
  # Lines
  x_pos_1 = 36 + blank_space + text_width_1 + blank_space / 2.0
  x_pos_2 = x_pos_1 + blank_space + text_width_2
  x_pos_3 = x_pos_2 + blank_space + text_width_3
  draw_line(36, 585, 576, 585, width = 3.0)
  draw_line(x_pos_1, 490, x_pos_1, 490 + 50, width = 3.0)
  draw_line(x_pos_2, 490, x_pos_2, 490 + 50, width = 3.0)
  draw_line(x_pos_3, 490, x_pos_3, 490 + 50, width = 3.0)
  
  # Second row logos
  frame_width = 540 / 5.0
  NAIA_width = 60.0
  insert_image(36 + (frame_width - NAIA_width) / 2.0, 622, NAIA_width, NAIA_width * (607/1280.0), "./Division_logos/NAIA_logo_original.png", line_color = "None")
  NCAA_width = 50
  insert_image(36 + frame_width + (frame_width - NCAA_width) / 2.0, 608, NCAA_width, NCAA_width * (1179/1200.0), "./Division_logos/NCAA_DI_logo_original.png", line_color = "None")
  insert_image(36 + 2 * frame_width + (frame_width - NCAA_width) / 2.0, 608, NCAA_width, NCAA_width * (1179/1200.0), "./Division_logos/NCAA_DII_logo_original.png", line_color = "None")
  insert_image(36 + 3 *frame_width + (frame_width - NCAA_width) / 2.0, 608, NCAA_width, NCAA_width * (1179/1200.0), "./Division_logos/NCAA_DIII_logo_original.png", line_color = "None")
  NJCAA_height = 50; NJCAA_width = NJCAA_height * (344.0 / 307.0)
  insert_image(36 + 4 * frame_width + (frame_width - NJCAA_width) / 2.0, 608, NJCAA_width, NJCAA_height, "./Division_logos/NJCAA_DI_logo.png", line_color = "None")
  
  # Second row numbers
  text_width = frame_width; text_height = 66
  text_frame(36, 670, text_width, text_height, ["42", "players"], ["Pink Sans 130", "Pink Sans 130"], [50, 20])
  text_frame(36 + text_width, 670, text_width, text_height, ["60", "players"], ["Pink Sans 130", "Pink Sans 130"], [50, 20]) #57 indoors + 3 BVB
  text_frame(36 + 2 * text_width, 670, text_width, text_height, ["60", "players"], ["Pink Sans 130", "Pink Sans 130"], [50, 20])
  text_frame(36 + 3 * text_width, 670, text_width, text_height, ["35", "players"], ["Pink Sans 130", "Pink Sans 130"], [50, 20])
  text_frame(36 + 4 * text_width, 670, text_width, text_height, ["78", "players"], ["Pink Sans 130", "Pink Sans 130"], [50, 20])
  