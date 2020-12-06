#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (0, 0, 0, 0)

def text_frame(pos_x, pos_y, frame_width, frame_height, texts_list, fonts_list, font_sizes, colors, alignment = ALIGN_CENTERED, line_spacing = 24):
  this_text_frame = createText(pos_x, pos_y, frame_width, frame_height)
  insertText(texts_list[0] + "\n", -1, this_text_frame)
  setFont(fonts_list[0], this_text_frame); setFontSize(font_sizes[0], this_text_frame); setTextColor(colors[0], this_text_frame)
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
    selectText(previous_line_length, length_text_line, this_text_frame)
    setTextColor(colors[idx], this_text_frame)
    selectText(previous_line_length, length_text_line, this_text_frame)
    setTextAlignment(alignment, this_text_frame)
    previous_line_length += length_text_line + 1
  setTextAlignment(alignment, this_text_frame); setLineSpacing(line_spacing, this_text_frame)

def draw_line(x1, y1, x2, y2, line_type = LINE_DASH, width = 1, color = "Map Blue"):
  this_line = createLine(x1, y1, x2, y2); setLineStyle(line_type, this_line); setLineColor(color, this_line)
  setLineWidth(width, this_line)
  
def insert_image(pos_x, pos_y, img_width, img_height, location):
  this_image = createImage(pos_x, pos_y, img_width, img_height); loadImage(location, this_image); setScaleImageToFrame(1, 1, this_image)

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  # defineColor("AIC Yellow", 20, 27, 198, 3)
  
  insert_image(-0.5, 0, 616, 796, "NCAA_DII_cover.jpg")
  div_width = 185
  div_rect = createRect(612 - div_width, 0, div_width, 30)
  setFillColor("White", div_rect); setLineColor("White", div_rect)
  text_frame(612 - div_width + 4, 6, div_width, 35, ["NCAA Division II"], ["Asimov Print C"], [24], ["Black"], alignment = ALIGN_RIGHT)
  insert_image(30, 56, 70, 70 * (1179.0 / 1200), "./Division_logos/NCAA_DII_logo_original.png")
  text_frame(438, 705, 170, 70, ["Karla Santos", "California State University", "Los Angeles, California", "Photo: Robert Huskey"], ["Asimov Print C" for idx in range(4)], 4 * [12], 
             ["White" for idx in range(4)], alignment = ALIGN_RIGHT, line_spacing = 15)