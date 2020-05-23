import tkinter as tk
from random import randint

WIDTH = 800
HEIGHT = 600

def tick():
    global x, y
    global dx, dy
    #global ball_id, r

    x += dx
    y += dy

    if x >= WIDTH-r or x <= r:
        dx = -dx
    if y >= HEIGHT-r or y <= r:
        dy = -dy

    c.move(ball_id, dx, dy)
    root.after(20, tick)


def main():
    global root, c
    global ball_id, x, y, dx, dy, r

    root = tk.Tk()
    c = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    c.pack()

    r = randint(20, 50)
    x = randint(r, WIDTH-r)
    y = randint(r, HEIGHT-r)

    dx = randint(2, 5)
    dy = randint(2, 5)

    color = "#%02x%02x%02x" % (randint(0, 255), randint(0, 255), randint(0, 255))
    ball_id = c.create_oval(x-r, y-r, x+r, y+r, fill=color)

    tick()
    root.mainloop()

if __name__ == "__main__":
    main()