"""
Пробуем классы на зуб
"""

import tkinter as tk

class ball:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        c.create_oval(x-r, y-r, x+r, y+r, fill=color)

    


def main():
    global root, c

    root = tk.Tk()
    c = tk.Canvas(root, width="800", height="600")
    c.pack()

    b1 = ball(100, 100, 20, "red")

    b2 = ball(200, 100, 20, "yellow")

    b1.y = 120

    c.update()


    root.mainloop()

if __name__ == "__main__":
    main()
