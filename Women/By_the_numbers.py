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

def draw_line(x1, y1, x2, y2, line_type = LINE_DASH, color = "Map Blue"):
  this_line = createLine(x1, y1, x2, y2); setLineStyle(line_type, this_line); setLineColor(color, this_line)
  
def insert_image(pos_x, pos_y, img_width, img_height, location):
  this_image = createImage(pos_x, pos_y, img_width, img_height); loadImage(location, this_image); setScaleImageToFrame(1, 1, this_image)

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
  
  text_frame(36, 9, 540, 36, ["By the numbers"], ["OLD SPORT 02 ATHLETIC NCV Regular"], [24], color = "White")  
  text_frame(0, 6.7, 36, 36, ["2019", "-", "2020"], ["OLD SPORT 02 ATHLETIC NCV Regular" for idx in range(3)], [11,11, 11], color = "White", line_spacing = 7)
  text_frame(576, 6.7, 36, 36, ["2019", "-", "2020"], ["OLD SPORT 02 ATHLETIC NCV Regular" for idx in range(3)], [11,11, 11], color = "White", line_spacing = 7)
  
  draw_line(340, 36, 340, 756) # vertical line
  
  # Number of players
  text_frame(0, 50, 340, 87, ["274", "student athletes"], ["Pink Sans 130", "Pink Sans 130"], [70, 20])
  draw_line(0, 140, 340, 140)
  
  # Puerto Rico map
  insert_image(37, 141, 270, 132, "./../Maps/pr_map_filled.png")
  text_frame(0, 261, 340, 75, ["58", "municipalities"], ["Pink Sans 130", "Pink Sans 130"], [50, 20])
  draw_line(0, 334, 340, 334)
  
  # High School logos
  high_school_logos = ["Colegio Puertorriqueño de Niñas", "Colegio Católico Notre Dame", "Colegio del Sagrado Corazón de Jesús", 
                       "Academia Discípulos de Cristo", "Colegio San Benito", "Escuela Patria Latorre Ramírez",
                       "Colegio De La Salle", "Christian Military Academy"]
  for idx in range(len(high_school_logos)):
    if idx < 4: insert_image(50 + idx * 60, 346, 60, 60, "./Escuelas/" + high_school_logos[idx].replace(" ", "_") + ".png")
    else: insert_image(50 + (idx - 4) * 60, 346 + 60, 60, 60, "./Escuelas/" + high_school_logos[idx].replace(" ", "_") + ".png")
    
  text_frame(0, 472, 340, 75, ["77", "high schools in Puerto Rico"], ["Pink Sans 130", "Pink Sans 130"], [50, 20])
  draw_line(0, 545, 340, 545)
  
  # United States map
  insert_image(37, 551, 270, 142, "./../Maps/usa_map_filled.png")
  text_frame(0, 688, 340, 75, ["32", "states & Washington, D.C."], ["Pink Sans 130", "Pink Sans 130"], [50, 20])
  
