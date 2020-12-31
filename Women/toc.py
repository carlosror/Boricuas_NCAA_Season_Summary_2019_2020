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

sections_dict = {}; page_counter = 0
with open("Final_document_order.csv") as f:
  next(f) # skip headers row
  for line in f:
    current_line_list = line.split(",")
    section = current_line_list[0]
    if current_line_list[4] == "": num_pages = 0
    else: num_pages = int(current_line_list[4])
    sections_dict[section] = page_counter + 1
    page_counter += num_pages

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("Maine_MA_Blue", int(0.82*255), int(0.565*255), int(0.027*255), int(0.051*255))
  
  insert_image(-0.5, 0, 616, 796, "toc.jpg")
  # draw_line(200, 36, 200, 436, line_type = LINE_SOLID, width = 0.5, color = "White")
  frame_width = 190; frame_header_height = 40; frame_comment_height = 24; frame_div_height = 15; frame_width_2 = 160; sep = 10
  xpos_offset = 40; ypos_offset = 20; xpos_offset_2 = 435
  
  # Left side
  text_frame(xpos_offset, ypos_offset, frame_width, frame_div_height, ["NAIA"], ["Calibri Bold"], [15], ["Maine_MA_Blue"], alignment = ALIGN_RIGHT)
  FMU_page = sections_dict["Article: FMU Eight"]
  text_frame(xpos_offset, ypos_offset + 1 * frame_div_height, frame_width, frame_header_height, [str(FMU_page), "The FMU Eight"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_RIGHT, line_spacing = 15)
  text_frame(xpos_offset, ypos_offset + 1 * frame_div_height + 1 * (frame_header_height), frame_width, frame_comment_height, ["In South Florida, a Puerto Rican octet helps take FMU volleyball to rarefied heigths"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_RIGHT, line_spacing = 11)
  text_frame(xpos_offset, ypos_offset + 1 * frame_div_height + 1 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width, frame_div_height, ["NCAA DIVISION I"], ["Calibri Bold"], [15], ["Maine_MA_Blue"], alignment = ALIGN_RIGHT)
  Evansville_page = sections_dict["Article: Feliciano & Vázquez"]
  text_frame(xpos_offset, ypos_offset + 2 * frame_div_height + 1 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width, frame_header_height, [str(Evansville_page), "Feliciano & Vázquez"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_RIGHT, line_spacing = 15)
  text_frame(xpos_offset, ypos_offset+ 2 * frame_div_height + 2 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width, frame_comment_height, ["In Indiana, a pair of Aces"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_RIGHT, line_spacing = 11)
  Bernier_page = sections_dict["Article: Lina Bernier"]
  text_frame(xpos_offset, ypos_offset + 2 * frame_div_height + 2 * (frame_header_height) + 2 * (frame_comment_height) + 2 * sep, frame_width, frame_header_height, [str(Bernier_page), "Lina Bernier"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_RIGHT, line_spacing = 15)
  text_frame(xpos_offset, ypos_offset + 2 * frame_div_height + 3 * (frame_header_height) + 2 * (frame_comment_height) + 2 * sep, frame_width, frame_comment_height, ["In Miami, a most versatile performer"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_RIGHT, line_spacing = 11)
  Trujillo_page = sections_dict["Article: Mariana Trujillo"]
  text_frame(xpos_offset, ypos_offset+ 2 * frame_div_height + 3 * (frame_header_height) + 3 * (frame_comment_height) + 3 * sep, frame_width, frame_header_height, [str(Trujillo_page), "Mariana Trujillo"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_RIGHT, line_spacing = 15)
  text_frame(xpos_offset, ypos_offset + 2 * frame_div_height + 4 * (frame_header_height) + 3 * (frame_comment_height) + 3 * sep, frame_width, frame_comment_height, ["In Alabama, forever 17"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_RIGHT, line_spacing = 11)
  # Right side
  text_frame(xpos_offset_2, ypos_offset, frame_width_2, frame_div_height, ["NCAA DIVISION II"], ["Calibri Bold"], [15], ["Maine_MA_Blue"], alignment = ALIGN_LEFT)
  AIC_page = sections_dict["Article: Eckert & Serra"]
  text_frame(xpos_offset_2, ypos_offset + 1 * frame_div_height, frame_width_2, frame_header_height, [str(AIC_page), "Eckert & Serra"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_LEFT, line_spacing = 15)
  text_frame(xpos_offset_2, ypos_offset + 1 * frame_div_height + 1 * (frame_header_height), frame_width_2, frame_comment_height, ["In Massachusetts, a playmaker and a finisher"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_LEFT, line_spacing = 11)
  text_frame(xpos_offset_2, ypos_offset + 1 * frame_div_height + 1 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width_2, frame_div_height, ["NCAA DIVISION III"], ["Calibri Bold"], [15], ["Maine_MA_Blue"], alignment = ALIGN_LEFT)
  Manhattanville_page = sections_dict["Article: Vital & Figueroa"]
  text_frame(xpos_offset_2, ypos_offset + 2 * frame_div_height + 1 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width_2, frame_header_height, [str(Manhattanville_page), "Vital & Figueroa"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_LEFT, line_spacing = 15)
  text_frame(xpos_offset_2, ypos_offset+ 2 * frame_div_height + 2 * (frame_header_height) + 1 * (frame_comment_height) + sep, frame_width_2, frame_comment_height, ["In New York, a pair of underclassmen rise to the occasion"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_LEFT, line_spacing = 11)
  Perez_page = sections_dict["Article: María Pérez"]
  text_frame(xpos_offset_2, ypos_offset + 2 * frame_div_height + 2 * (frame_header_height) + 2 * (frame_comment_height) + 2 * sep, frame_width_2, frame_header_height, [str(Perez_page), "María Pérez"], 
             ["RACE1 Brannt NCV Regular", "Asimov Print C"], [24, 15], 2 *["White"], alignment = ALIGN_LEFT, line_spacing = 15)
  text_frame(xpos_offset_2, ypos_offset + 2 * frame_div_height + 3 * (frame_header_height) + 2 * (frame_comment_height) + 2 * sep, frame_width_2, frame_comment_height, ["In Maine, a senior puts the finishing touches on her college career"], 
             ["Calibri Regular"], [10.8], ["White"], alignment = ALIGN_LEFT, line_spacing = 11)
  
  # Departments
  text_frame(xpos_offset_2, ypos_offset+ 1 * frame_div_height + 3 * (frame_header_height) + 3 * (frame_comment_height) + 6 * sep, frame_width_2, frame_div_height, ["Departments"], ["Arial Black"], [12], ["Maine_MA_Blue"], alignment = ALIGN_LEFT)
  NAIA_page = sections_dict["NAIA Cover"]; NCAA_page = sections_dict["NCAA DI Cover"]; NJCAA_page = sections_dict["NJCAA DI Cover"]
  Beach_VB_page = sections_dict["Beach Volleyball Cover"]; LAI_page = sections_dict["LAI cover"]; Where_they_play_page = sections_dict["Where they play - Wordcloud"]
  Where_they_are_from_page = sections_dict["Where they are from - Wordcloud"]; All_Conf_page = sections_dict["All Conference - Cover"]
  All_Academic_page = sections_dict["All Academic - Cover"]; Stat_leaders_page = sections_dict["Statitical leaders cover"]; Clubs_page = sections_dict["Clubs - Cover"]
  National_tournaments_page = sections_dict["National tournaments - Cover"]; Outstanding_matches_page = sections_dict["Outstanding matches - Cover"]
  departments_pages = [str(NAIA_page), str(NCAA_page), str(NJCAA_page), str(Beach_VB_page), str(LAI_page), str(Where_they_play_page), str(Where_they_are_from_page),
                       str(All_Conf_page), str(All_Academic_page), str(Stat_leaders_page), str(Clubs_page), str(National_tournaments_page), str(Outstanding_matches_page)]
  dpt_num_lines = len(departments_pages)
  text_frame(xpos_offset_2, ypos_offset+ 2 * frame_div_height + 3 * (frame_header_height) + 3 * (frame_comment_height) + 6.5 * sep, frame_width_2 / 8.0, 
             11 * frame_div_height, departments_pages, dpt_num_lines * ["Asimov Print C"], dpt_num_lines * [10], dpt_num_lines * ["White"], alignment = ALIGN_LEFT, line_spacing = 12)
  departments = ["NAIA", "NCAA", "NJCAA", "Beach Volleyball", "L.A.I.", "Where They Play", "Where They Are From", 
                 "All-Conference", "Academic All-Stars", "Statistical Leaders", "Clubs", "National Tournaments", "Outstanding Matches"]
  text_frame(xpos_offset_2 + 30, ypos_offset + 2 * frame_div_height + 3 * (frame_header_height) + 3 * (frame_comment_height) + 6.5 * sep, 
             frame_width_2 * 0.8, 11 * frame_div_height, departments, dpt_num_lines * ["Asimov Print C"], dpt_num_lines * [10], dpt_num_lines * ["White"], alignment = ALIGN_LEFT, line_spacing = 12)
  