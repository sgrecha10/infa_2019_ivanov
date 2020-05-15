"""
Evil  smile
version 1.0

sgrecha10@gmail.com

"""

from graph import *

def circle_full(x, y, r, colorpen, colorbrush):
    penSize(1)
    penColor(colorpen)
    brushColor(colorbrush)
    circle(x, y, r)

circle_full(250, 200, 100, 'black', (255,255,0))
circle_full(200, 180, 20, 'black', (255,0,0))
circle_full(300, 180, 15, 'black', (255,0,0))

circle_full(200, 180, 7, 'black', (0,0,0))
circle_full(300, 180, 7, 'black', (0,0,0))

penSize(20)
line(210,250, 290, 250)

penSize(10)
line(235,180, 160, 110)

penSize(10)
line(275,180, 360, 110)

run()