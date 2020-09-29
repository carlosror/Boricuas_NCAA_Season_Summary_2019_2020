#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)
if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):
  try:
    execfile("NCAA_DII_mugshots_3_noNewDoc2.py")
  except SystemExit:
    newPage(-1)
  try:
    execfile("NCAA_DII_mugshots_3_noNewDoc.py")
  except SystemExit:
    newPage(-1)
  try:
    execfile("NCAA_DII_mugshots_3_noNewDoc2.py")
  except SystemExit:
    newPage(-1)
  try:
    execfile("NCAA_DII_mugshots_3_noNewDoc.py")
  except SystemExit:
    newPage(-1)
  newPage(-1)
  # gotoPage(4)
  # exit()