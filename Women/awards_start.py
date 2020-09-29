#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  
  top_rect = createRect(0, 0, 612, 36)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  bottom_rect = createRect(0, 756, 612, 36)
  setFillColor("NJCAA Blue", bottom_rect); setLineColor("NJCAA Blue", bottom_rect)
  
  first_rect = createRect(0, 36, 306, 180)
  setFillColor("NJCAA Gray", first_rect); setLineColor("NJCAA Gray", first_rect)
  
  pic_1 = createImage(306, 36, 306, 180)
  loadImage("Lina_Bernier_sample_cropped.jpg", pic_1)
  setScaleImageToFrame(1, 1, pic_1)
  
  ribbon_banner = createImage(72, 60, 162, 30)
  loadImage("ribbon_banner.png", ribbon_banner)
  setScaleImageToFrame(1, 1, ribbon_banner)
  
  # defineColor("FIU Gold", 16, 34, 84, 3)
  # rect_1_logo = createRect(572, 36, 40, 40)
  # setFillColor("FIU Gold", rect_1_logo); # setLineColor("White", rect_1_logo)
  # pic_1_logo = createImage(572, 36, 40, 40)
  # loadImage("FIU_logo.gif", pic_1_logo)
  # setScaleImageToFrame(1, 1, pic_1_logo)
  # rect_1_name = createRect(572, 76, 40, 140)
  # setFillColor("FIU Gold", rect_1_name); # setLineColor("White", rect_1_name)
  # first_name = createText(572, 86, 40, 14)
  # setText("LINA", first_name)
  # setFont("Asimov Print C", first_name); setFontSize(12, first_name)
  # setTextAlignment(ALIGN_CENTERED, first_name)
  # last_name = createText(572, 120, 130, 24)
  # setText("BERNIER", last_name)
  # setFont("Asimov Print C", first_name); setFontSize(22, last_name)
  # setTextAlignment(ALIGN_CENTERED, last_name)
  # rotateObject(-90, last_name)
  # moveObject(30, -35, last_name)
  
  second_rect = createRect(306, 216, 306, 180)
  setFillColor("NJCAA Blue", second_rect); setLineColor("NJCAA Blue", second_rect)
  
  pic_2 = createImage(0, 216, 306, 180)
  loadImage("Alejandra_Delgado_sample_cropped.jpg", pic_2)
  setScaleImageToFrame(1, 1, pic_2)
  
  third_rect = createRect(0, 396, 306, 180)
  setFillColor("NJCAA Blue", third_rect); setLineColor("NJCAA Blue", third_rect)
  
  pic_3 = createImage(306, 396, 306, 180)
  loadImage("Alejandra_Rodríguez_3_sample_cropped.jpg", pic_3)
  setScaleImageToFrame(1, 1, pic_3)
  
  fourth_rect = createRect(306, 576, 306, 180)
  setFillColor("NJCAA Gray", fourth_rect); setLineColor("NJCAA Gray", fourth_rect)
  
  pic_4 = createImage(0, 576, 306, 180)
  loadImage("Andrea_Laboy_4_sample_cropped.jpg", pic_4)
  setScaleImageToFrame(1, 1, pic_4)