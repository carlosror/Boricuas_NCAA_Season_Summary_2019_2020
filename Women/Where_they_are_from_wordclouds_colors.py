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

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
  
  text_frame(0, 9, 612, 36, ["Where they are from"], ["OLD SPORT 02 ATHLETIC NCV Regular"], [24], colors = ["White"])
  text_frame(0, 6.7, 36, 36, ["2019", "-", "2020"], ["OLD SPORT 02 ATHLETIC NCV Regular" for idx in range(3)], [11,11, 11], 
             colors = ["White" for idx in range(3)], line_spacing = 7)
  text_frame(576, 6.7, 36, 36, ["2019", "-", "2020"], ["OLD SPORT 02 ATHLETIC NCV Regular" for idx in range(3)], [11,11, 11], 
             colors = ["White" for idx in range(3)], line_spacing = 7)
  
  wordcloud1_height = 540 * (1642 / 2510.0)
  offset = 80
  insert_image(36, offset, 540, wordcloud1_height, "wordcloud_hometowns_colors3_scaled.png")
  wordcloud2_height = 540 * (1402 / 2818.0)
  insert_image(36, offset + wordcloud1_height + 10, 540, wordcloud2_height, "wordcloud_highschools_colors7_scaled.png")
  space_rect = createRect(36, offset + wordcloud1_height - 1, 540, 12)
  setFillColor("White", space_rect); setLineColor("None", space_rect)
  
  draw_line(36, offset + wordcloud1_height + 5, 576, offset + wordcloud1_height + 5, line_type = LINE_SOLID, width = 0.5, color = "Cyan")
  
  wordcloud_label_1_ypos = offset + wordcloud1_height + 5 - 40
  wordcloud_label_1 = createRect(36, wordcloud_label_1_ypos, 75, 40)
  setFillColor("Cyan", wordcloud_label_1); setLineColor("None", wordcloud_label_1)
  
  text_frame(36, wordcloud_label_1_ypos + 5, 75, 50, ["58", "municipalities"], ["Pink Sans 130" for idx in range(2)], [24, 12], colors = ["White" for idx in range(2)], line_spacing = 13)
  
  wordcloud_label_2_ypos = offset + wordcloud1_height + 5
  wordcloud_label_2 = createRect(36 + 540 - 75, wordcloud_label_2_ypos, 75, 40)
  setFillColor("Cyan", wordcloud_label_2); setLineColor("None", wordcloud_label_2)
  
  text_frame(36 + 540 - 75, wordcloud_label_2_ypos + 5, 75, 50, ["77", "high schools"], ["Pink Sans 130" for idx in range(2)], [24, 12], colors = ["White" for idx in range(2)], line_spacing = 13)
  