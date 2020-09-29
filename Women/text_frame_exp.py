#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  my_text = createText(36, 36, 540, 756, "my_text")
  setText("Hello, my name is Carlos. I love Scribus. ", my_text)
  selectText(0, 5, my_text)
  setFont("Playball Regular", my_text)
  # setFontSize(18, my_text)
  
