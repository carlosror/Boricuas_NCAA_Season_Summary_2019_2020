#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

# Dictionary of logos' height/width aspect ratios. It is used to position the school logo
# There's no way to programatically adjust frame to image.
# The Python Scribus uses doesn't have any image utilities like PIL so I could not
# figure out a way to determine the image's aspect ratio programatically. :|
# There is a program I wrote called Logo_aspect_ratio.py that takes all the images files
# in a directory and generates a CSV file of their width and height. The program is located in 
# the Women directory. After you run that program, you can run this one.

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  # Define colors and create headers
  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
  defineColor("NAIA Red", 8, 237, 198, 18)
  defineColor("NCAA Blue", 230, 163, 0, 0)
  defineColor("173F5F", 217, 156, 63, 108)
  defineColor("20639B", 208, 136, 18, 33)
  defineColor("3CAEA3", 172, 14, 96, 11)
  defineColor("F6D55C", 15, 34, 182, 4)
  defineColor("ED553B", 4, 200, 203, 3)
    
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
  center_rect = createRect(0, 36, 612, 720)
  setFillColor("NJCAA Gray", center_rect); setLineColor("NJCAA Gray", center_rect)
    
  page_header = createText(36, 9, 540, 36)
  setText("What they study", page_header)
  setTextColor("White", page_header)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", page_header); setFontSize(26, page_header)
  setTextAlignment(ALIGN_CENTERED, page_header)
  
  years1 = createText(0, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years1)
  years2 = createText(576, 6.7, 36, 36); setText("2019" + "\n" + "-" + "\n" + "2020", years2)
  setTextColor("White", years1); setTextColor("White", years2)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", years1); setFontSize(11, years1); setTextAlignment(ALIGN_CENTERED, years1)
  setFont("OLD SPORT 02 ATHLETIC NCV Regular", years2); setFontSize(11, years2); setTextAlignment(ALIGN_CENTERED, years2)
  setLineSpacing(7, years1); setLineSpacing(7, years2)
  
  # Insert barplot
  barplot_x = 36; barplot_y = 50; barplot_w = 540; barplot_h = 290
  barplot = createImage(barplot_x, barplot_y, barplot_w, barplot_h)
  loadImage("major_categories.png", barplot); setScaleImageToFrame(1, 1, barplot)
  
  # Small banner towards the middle
  small_banner_y = barplot_y + 306
  small_banner_h = 24
  small_banner = createRect(barplot_x, small_banner_y, barplot_w, small_banner_h)
  setFillColor("NJCAA Blue", small_banner); setLineColor("NJCAA Blue", small_banner)
  small_banner_text = createText(barplot_x, small_banner_y + 3, barplot_w, small_banner_h)
  setText("Most popular majors by career field", small_banner_text); setTextColor("White", small_banner_text)
  setFont("Playball Regular", small_banner_text); setFontSize(20, small_banner_text); setTextAlignment(ALIGN_CENTERED, small_banner_text)
  
  career_dict = {0: "Business", 1: "Health and Medicine", 2: "S.T.E.M.", 3: "Social Sciences", 4: "Other"}
  career_dict_color = {"Business": "173F5F", "Health and Medicine": "20639B", "S.T.E.M.": "3CAEA3" , "Social Sciences": "F6D55C", "Other": "ED553B"}
  for career in career_dict.keys():
    table_w = 175
    if career > 2: 
      table_x = 36 + (career - 3) * (table_w + 7.5)
      table_y = (small_banner_y + 40) + 110 
    else: 
      table_x = 36 + career * (table_w + 7.5)
      table_y = (small_banner_y + 40)
    table_header_height = 20
    table_header = createRect(table_x, table_y, table_w, table_header_height)
    setFillColor(career_dict_color[career_dict[career]], table_header); setLineColor(career_dict_color[career_dict[career]], table_header)
    table_header_text = createText(table_x, table_y + 3, table_w, table_header_height)
    setText(career_dict[career], table_header_text); setTextColor("White", table_header_text)
    setFont("Asimov Print C", table_header_text); setFontSize(17, table_header_text); #setTextAlignment(ALIGN_CENTERED, table_header_text)
    
    num_rows = 5
    row_h = 16
    for row in range(num_rows):
      this_row = createRect(table_x, (table_y + table_header_height + row * row_h), table_w, row_h)
      if ((row + 1) % 2) == 0:
        setFillColor("Darker Gray", this_row); setLineColor("Darker Gray", this_row)
      else:
        setFillColor("White", this_row); setLineColor("White", this_row)
        
    major_counts_frame_majors = createText(table_x, table_y + table_header_height + 3, 0.9 * table_w, 10 * row_h + 4)
    major_counts_frame_num = createText(table_x + 0.9 * table_w, table_y + table_header_height + 3, 0.1 * table_w, 10 * row_h + 4)
    with open("major_counts_" + career_dict[career].replace(" ", "_").replace(".", "") + ".csv") as f2:
      next(f2)
      for line in f2:
        current_line_list = line.split(",")
        insertText(current_line_list[0] + "\n", -1, major_counts_frame_majors)
        insertText(current_line_list[1] + "\n", -1, major_counts_frame_num)
        
    setFont("Asimov Print C", major_counts_frame_majors); setFontSize(11, major_counts_frame_majors)
    setTextColor("NJCAA Blue", major_counts_frame_majors); setLineSpacing(16.1, major_counts_frame_majors)
    setFont("Asimov Print C", major_counts_frame_num); setFontSize(12, major_counts_frame_num)
    setTextColor("NJCAA Blue", major_counts_frame_num); setLineSpacing(8.1, major_counts_frame_num); setTextAlignment(ALIGN_RIGHT, major_counts_frame_num)
    
  # Asterisks:
  header_asterisk = createText(430, 9, 12, 36)
  setText("*", header_asterisk); setTextColor("White", header_asterisk); setFontSize(18, header_asterisk)
  
  stem_asterisk_1 = createText(340, 300, 12, 36)
  setText("**", stem_asterisk_1); setTextColor("Black", stem_asterisk_1); setFontSize(12, stem_asterisk_1)
  
  stem_asterisk_2 = createText(465, 398, 16, 36)
  setText("**", stem_asterisk_2); setTextColor("White", stem_asterisk_2); setFontSize(18, stem_asterisk_2)
  
  footer_asterisk = createText(36, 760, 6, 34)
  setText("*", footer_asterisk); setTextColor("White", footer_asterisk); setFontSize(9, footer_asterisk)
  
  footer_asterisk_2 = createText(36, 772, 10, 34)
  setText("**", footer_asterisk_2); setTextColor("White", footer_asterisk_2); setFontSize(9, footer_asterisk_2)
  
  footnote_frame = createText(40, 760, 536, 35)
  footnote = "Majors pursued by 144 student athletes from 4-year institutions." 
  setText(footnote, footnote_frame); setTextColor("White", footnote_frame); setFontSize(9, footnote_frame); setLineSpacing(9, footnote_frame)
  
  footnote_frame_2 = createText(44, 772, 536, 35)
  footnote_2 = "S.T.E.M. = Science, Technology, Engineering, and Mathermatics" 
  setText(footnote_2, footnote_frame_2); setTextColor("White", footnote_frame_2); setFontSize(9, footnote_frame_2); setLineSpacing(9, footnote_frame_2)