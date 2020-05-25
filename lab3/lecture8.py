import tkinter as tk
from random import randint


WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self):
        self.r = randint(20, 50)
        self.x = randint(self.r, WIDTH - self.r)
        self.y = randint(self.r, HEIGHT - self.r)
        self.dx = randint(-5, 5)
        self.dy = randint(-5, 5)
        """
        self.color = "#%02x%02x%02x" % (randint(0, 255),
                                        randint(0, 255),
                                        randint(0, 255))
        """
        #self.w = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.w = tuple((randint(0, 255) for i in range(3)))

        self.color = "#%02x%02x%02x" % (self.w)
        self.ball_id = c.create_oval(self.x - self.r,
                                     self.y - self.r,
                                     self.x + self.r,
                                     self.y + self.r, fill=self.color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x >= WIDTH - self.r or self.x <= self.r:
            self.dx = -self.dx
        if self.y >= HEIGHT - self.r or self.y <= self.r:
            self.dy = -self.dy

    def show(self):
        c.move(self.ball_id, self.dx, self.dy)


def tick():
    for b in bs:
        b.move()
        b.show()
    root.after(20, tick)


def main():
    global root, c, bs

    root = tk.Tk()
    c = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    c.pack()

    bs = [Ball() for i in range(40)]

    """
    bs = []
    for i in range(5):
        bs.append(Ball())
    """

    print((bs))

    tick()
    root.mainloop()

if __name__ == "__main__":
    main()