#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *

margins = (36, 36, 0, 0)

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  myText = createText(40, 40, 100, 100)
  insertText("Hello, \n", -1, myText)
  insertText("World", -1, myText)
  selectText(0, 5, myText)
  setTextColor("Red", myText); setFont("Playball Regular", myText)
  selectText(0, 5, myText)
  setFontSize(30, myText)
  selectText(0, 5, myText)
  setTextAlignment(ALIGN_CENTERED, myText)