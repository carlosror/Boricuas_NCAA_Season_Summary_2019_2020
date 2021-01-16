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

filenames_list = []; num_pages_list = []; page_numbers_list = [];  page_counter = 0
                       
with open("Final_document_order.csv") as f:
  next(f) # skip headers row
  for line in f:
    current_line_list = line.split(",")
    filename = current_line_list[1]
    if current_line_list[4] == "": num_pages = 0
    else: num_pages = int(current_line_list[4])
    filenames_list.append(filename); num_pages_list.append(num_pages)
    page_numbers_list.append(page_counter + 1)
    page_counter += num_pages

# Pages for which we don't want page numbers
no_page_number_list = ["cover.sla", "toc.sla", "./Articles/Lina_Bernier_article/Bernier_poster.sla", 
                       "./Articles/Maria_Perez/Perez_poster.sla"]
no_page_number_list_2 = [page_numbers_list[filenames_list.index(section)] for section in no_page_number_list]
                       
if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):
  for idx in range(len(filenames_list)):
    pages_list = [page for page in range(1, num_pages_list[idx] + 1)]
    pages_tuple = tuple(pages_list) # input to importPage() must be a tuple
    importPage(filenames_list[idx], pages_tuple)
  deletePage(1)
  
  # Add page numbers
  num_pages = pageCount()
  for idx in range(1, num_pages + 1):
    if idx in no_page_number_list_2: continue
    gotoPage(idx)
    text_frame(576, 756, 36, 36, ["\n\n " + str(idx)], ["Asimov Print C"], [12], ["White"], line_spacing = 11)
  
  # Issue with article losing frame links from one page to another
  unlinkTextFrames("Evansville4")
  for idx in range(2,5):
    linkTextFrames("Evansville" + str(idx), "Evansville" + str(idx + 1))
  
  for idx in range(4,14,2):
    unlinkTextFrames("Fuentes" + str(idx))
  for idx in range(2,12):
    linkTextFrames("Fuentes" + str(idx), "Fuentes" + str(idx + 1))
  
  for idx in range(4,8,2):
    unlinkTextFrames("AIC" + str(idx))
  for idx in range(2,6):
    linkTextFrames("AIC" + str(idx), "AIC" + str(idx + 1))
  
  for idx in range(4,10,2):
    unlinkTextFrames("FMU" + str(idx))
  for idx in range(2,9):
    linkTextFrames("FMU" + str(idx), "FMU" + str(idx + 1))
  
  for idx in range(4,10,2):
    unlinkTextFrames("Bernier" + str(idx))
  for idx in range(2,9):
    linkTextFrames("Bernier" + str(idx), "Bernier" + str(idx + 1))
  
  for idx in range(4,8,2):
    unlinkTextFrames("Perez" + str(idx))
  for idx in range(2,6):
    linkTextFrames("Perez" + str(idx), "Perez" + str(idx + 1))
    
  for idx in range(4,8,2):
    unlinkTextFrames("Trujillo" + str(idx))
  for idx in range(2,7):
    linkTextFrames("Trujillo" + str(idx), "Trujillo" + str(idx + 1))
  
  for idx in range(4,8,2):
    unlinkTextFrames("Vital" + str(idx))
  for idx in range(2,6):
    linkTextFrames("Vital" + str(idx), "Vital" + str(idx + 1))