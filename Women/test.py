#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

defineColor("NJCAA Blue", 217, 168, 55, 94)
defineColor("NJCAA Gray", 0, 0, 0, 40)
defineColor("NJCAA Gray 2", 0, 0, 0, 153)
defineColor("NJCAA Blue 2", 221, 168, 15, 30)

right_rect = createRect(1, 1, 1, 1)
setFillColor("NJCAA Gray 2", right_rect); setLineColor("NJCAA Gray 2", right_rect)