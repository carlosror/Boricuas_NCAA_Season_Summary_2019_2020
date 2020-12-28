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

  defineColor("Maine_MA_Blue", int(0.82*255), int(0.565*255), int(0.027*255), int(0.051*255))
  
  insert_image(-0.5, 0, 616, 796, "toc.jpg")
  # draw_line(200, 36, 200, 436, line_type = LINE_SOLID, width = 0.5, color = "White")
  frame_width = 190; frame_header_height = 40; frame_comment_height = 24; frame_div_height = 15; frame_width_2 = 160; sep = 10
  xpos_offset = 40; ypos_offset = 20; xpos_offset_2 = 435
  
  # Left side
  text_frame(xpos_offset, ypos_offset, frame_width, frame_div_height, ["NAIA"], ["Calibri Bold"], [15], ["Maine_MA_Blue"], alignment = ALIGN_RIGHT)
  text_frame(xpos_offset, ypos_offset + 1 * frame_div_height, frame_width, frame_header_height, ["21", "The FMU Eight"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_RIGHT, line_spacing = 15)
  text_frame(xpos_offset, ypos_offset + 1 * frame_div_height + 1 * (frame_header_height), frame_width, frame_comment_height, ["In South Florida, a Puerto Rican octet helps take FMU volleyball to rarefied heigths"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_RIGHT, line_spacing = 11)
  text_frame(xpos_offset, ypos_offset + 1 * frame_div_height + 1 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width, frame_div_height, ["NCAA DIVISION I"], ["Calibri Bold"], [15], ["Maine_MA_Blue"], alignment = ALIGN_RIGHT)
  text_frame(xpos_offset, ypos_offset + 2 * frame_div_height + 1 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width, frame_header_height, ["32", "Feliciano & Vázquez"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_RIGHT, line_spacing = 15)
  text_frame(xpos_offset, ypos_offset+ 2 * frame_div_height + 2 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width, frame_comment_height, ["In Indiana, a pair of Aces"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_RIGHT, line_spacing = 11)
  text_frame(xpos_offset, ypos_offset + 2 * frame_div_height + 2 * (frame_header_height) + 2 * (frame_comment_height) + 2 * sep, frame_width, frame_header_height, ["43", "Lina Bernier"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_RIGHT, line_spacing = 15)
  text_frame(xpos_offset, ypos_offset + 2 * frame_div_height + 3 * (frame_header_height) + 2 * (frame_comment_height) + 2 * sep, frame_width, frame_comment_height, ["In Miami, a most versatile performer"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_RIGHT, line_spacing = 11)
  text_frame(xpos_offset, ypos_offset+ 2 * frame_div_height + 3 * (frame_header_height) + 3 * (frame_comment_height) + 3 * sep, frame_width, frame_header_height, ["54", "Mariana Trujillo"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_RIGHT, line_spacing = 15)
  text_frame(xpos_offset, ypos_offset + 2 * frame_div_height + 4 * (frame_header_height) + 3 * (frame_comment_height) + 3 * sep, frame_width, frame_comment_height, ["In Alabama, forever 17"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_RIGHT, line_spacing = 11)
  # Right side
  text_frame(xpos_offset_2, ypos_offset, frame_width_2, frame_div_height, ["NCAA DIVISION II"], ["Calibri Bold"], [15], ["Maine_MA_Blue"], alignment = ALIGN_LEFT)
  text_frame(xpos_offset_2, ypos_offset + 1 * frame_div_height, frame_width_2, frame_header_height, ["65", "Eckert & Serra"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_LEFT, line_spacing = 15)
  text_frame(xpos_offset_2, ypos_offset + 1 * frame_div_height + 1 * (frame_header_height), frame_width_2, frame_comment_height, ["In Massachusetts, a playmaker and a finisher"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_LEFT, line_spacing = 11)
  text_frame(xpos_offset_2, ypos_offset + 1 * frame_div_height + 1 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width_2, frame_div_height, ["NCAA DIVISION III"], ["Calibri Bold"], [15], ["Maine_MA_Blue"], alignment = ALIGN_LEFT)
  text_frame(xpos_offset_2, ypos_offset + 2 * frame_div_height + 1 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width_2, frame_header_height, ["76", "Vital & Figueroa"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_LEFT, line_spacing = 15)
  text_frame(xpos_offset_2, ypos_offset+ 2 * frame_div_height + 2 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width_2, frame_comment_height, ["In New York, a pair of underclassmen rise to the occasion"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_LEFT, line_spacing = 11)
  text_frame(xpos_offset_2, ypos_offset + 2 * frame_div_height + 2 * (frame_header_height) + 2 * (frame_comment_height) + 2 * sep, frame_width_2, frame_header_height, ["87", "María Pérez"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_LEFT, line_spacing = 15)
  text_frame(xpos_offset_2, ypos_offset + 2 * frame_div_height + 3 * (frame_header_height) + 2 * (frame_comment_height) + 2 * sep, frame_width_2, frame_comment_height, ["In Maine, a senior puts the finishing touches on her college career"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_LEFT, line_spacing = 11)
  
  text_frame(xpos_offset_2, ypos_offset+ 2 * frame_div_height + 3 * (frame_header_height) + 3 * (frame_comment_height) + 6 * sep, frame_width_2, frame_div_height, ["Departments"], ["Arial Black"], [12], ["Maine_MA_Blue"], alignment = ALIGN_LEFT)
  text_frame(xpos_offset_2, ypos_offset+ 3 * frame_div_height + 3 * (frame_header_height) + 3 * (frame_comment_height) + 6* sep, frame_width_2, frame_div_height, ["7      Meet the players"], ["Asimov Print C"], [10], ["White"], alignment = ALIGN_LEFT)
  text_frame(xpos_offset_2, ypos_offset+ 4 * frame_div_height + 3 * (frame_header_height) + 3 * (frame_comment_height) + 6 * sep, frame_width_2, frame_div_height, ["28     Meet the players"], ["Asimov Print C"], [10], ["White"], alignment = ALIGN_LEFT)
