"""
1_1.png
"""

from graph import *

def main():
    windowSize(600, 402)
    canvasSize(600, 402)

    draw_wrapper_and_colors()
    draw_waves()
    draw_sun()
    draw_umbrella()
    draw_ship() 
    draw_clouds_circle()
    draw_clouds_oval(330, 50, 25)

    run()

def draw_wrapper_and_colors():
    # wrapper
    penColor(0, 0, 0)
    penSize(1)
    brushColor(161, 245, 255)
    rectangle(0, 0, 600, 402)

    # turquoise
    brushColor(161, 245, 255)
    rectangle(0, 0, 600, 402)

    # blue
    brushColor(68, 35, 223)
    rectangle(0, 185, 600, 280)

    # yellow
    brushColor(255, 255, 0)
    rectangle(0, 280, 600, 402)


def draw_waves():
    # wave
    def wave_circle(x, y, r, color):
        penColor(color)
        penSize(1)
        brushColor(color)
        circle(x, y, r)
    for i in range(6):
        x1 = i * 100 + 25
        x2 = x1 + 50
        wave_circle(x2, 245, 40, (68, 35, 223))
        wave_circle(x1, 310, 40, (255, 255, 0))

def draw_sun():
    # sun
    penColor(255, 255, 255)
    brushColor(255, 255, 0)
    circle(530, 60, 40)

def draw_umbrella():
    # umbrella
    penColor(227, 130, 25)
    brushColor(227, 130, 25)
    rectangle(90, 235, 95, 385)

    penColor(172, 57, 57)
    brushColor(244, 81, 81)
    polygon([(90, 235), (95, 235), (160, 265), (25, 265), (90, 235)])

    penColor(224, 76, 98)
    polyline([(90, 235), (95, 235), (95, 265), (90, 235)])

    penColor(172, 57, 57)

    line(90, 235, 40, 265)
    line(90, 235, 60, 265)
    line(90, 235, 80, 265)

    line(95, 235, 105, 265)
    line(95, 235, 125, 265)
    line(95, 235, 145, 265)

def draw_ship():
    # ship
    brushColor(186, 80, 5)
    rectangle(350, 205, 500, 230)
    polygon([(500, 205), (560, 205), (500, 230)])
    arc(325, 180, 375, 230, 270, 180, PIESLICE)

    penColor('black')
    penSize(3)
    brushColor('white')
    circle(512, 214, 7)

    penColor('black')
    penSize(6)
    line(410, 120, 410, 205)

    penColor('gray')
    penSize(1)
    brushColor(222, 213, 153)
    polygon([(411, 120), (465, 160), (430, 160), (411, 120)])
    polygon([(411, 205), (430, 160), (465, 160), (411, 205)])

def draw_clouds_circle():
    penColor(150, 150, 150)
    brushColor(255, 255, 255)
    circle(130, 50, 15)
    circle(150, 50, 15)

    circle(120, 63, 15)
    circle(140, 65, 15)
    circle(160, 65, 15)

    circle(170, 50, 15)

    circle(180, 65, 15)

def oval_new(x, y, r):
    R = r * 1.2
    x1 = x - r
    y1 = y - R
    x2 = x + r
    y2 = y + R
    oval(x1, y1, x2, y2)


def draw_clouds_oval(x, y, r):
    penColor(150, 150, 150)
    brushColor(255, 255, 255)
    # r = 15
    # x = 130
    # y = 50

    oval_new(x, y, r)
    oval_new(x + 1.3*r, y, r)

    oval_new(x - 0.7*r, y + r, r)
    oval_new(x + 0.7*r, y + r, r)
    oval_new(x + 2*r, y + r, r)

    oval_new(x + 2.7*r, y, r)

    oval_new(x + 3.3*r, y + r, r)


main()