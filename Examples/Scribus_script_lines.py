#!/usr/bin/env python

from scribus import *

'''
An exercise with loops and tested against 1.4.3 Uses

newDocument
createLine
setLineWidth
setLineColor
setFillShade
createRect
saveDocAs
'''

Margins = (10, 10, 10, 10)
if newDocument(PAPER_A4, Margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

   #some constants
   a = 5      #line width
   b="Blue"
   m=33      #Fill shade, integer 0-100
   g60="Red"
   spx=30      #Start X
   spy=30      #Start Y
   a4w=595             #Width A4 getPageSize ?
   a4d=842             #depth A4 getPageSize ?

   #Draw the lines
   d = createLine(spx-a/2,spy,a4w-30+a/2,spy) #Top
   setLineColor(g60, d)
   setLineWidth(a, d)
   e = createLine(spx,spy,spx,a4d-27)  #LH vertical
   setLineWidth(a, e)
   setLineColor(g60, e)
   f = createLine(a4w-30,spy,a4w-30,a4d-27)	#RH vertical
   setLineWidth(a, f)
   setLineColor(g60, f)
   g = createLine(spx-a/2,a4d-27,a4w-30+a/2,a4d-27)#Bottom
   setLineWidth(a, g)
   setLineColor(g60, g)

   #Draw the "holes"
   for i in range(0,int(770/10)):
       l = createRect(spx+5,spy+10+10*i,10,5)
       setFillShade(m,l)
       setLineColor(g60,l)		
   for i in range(0,int(770/10)):
       k = createRect(a4w-45,spy+10+10*i,10,5)
       setFillShade(m,k)		
       setLineColor(g60,k)

   saveDocAs("Fancy_border.sla") #Make sure this is writable