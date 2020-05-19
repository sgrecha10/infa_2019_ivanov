from tkinter import *
from random import randrange as rnd, choice
import time

i = 0  # Счетчик очков

root = Tk()
root.geometry('800x600')

label_score = Label(root, bg='black', fg='white', width=20)
label_score.pack()

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)



colors = ['red', 'orange', 'yellow', 'green', 'blue']


def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(10, 50)
    global fig
    fig = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    motion()
    #for i in range(100):
        #pass
        #canv.move(fig, 10, 10)

    root.after(1000, new_ball)


def click(event):
    print(x, y, r)
    print(event.x, event.y)

    global i

    length = (abs(x - event.x) ** 2 + abs(y - event.y)) ** 0.5

    if length <= r:
        i += 1

    print(i)
    label_score['text'] = i

def motion():
    canv.move(fig, 1, 0)
    if canv.coords(fig)[2] < 800:
        root.after(10, motion)


"""
def move_points(figure):
    delta_x = rnd(-10, 10)
    delta_y = rnd(-10, 10)
    for i in range(100):
        canv.move(figure, delta_x, delta_y)
"""


new_ball()
canv.bind('<Button-1>', click)

mainloop()
