import tkinter as tk
import math
from random import randint, choice

WIDTH = 800
HEIGHT = 600


class Ball:
    #def __init__(self, r, x, y, dx, dy):
    def __init__(self):
        """
        self.r = r
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        """
        self.r = randint(50, 50)
        self.x = randint(self.r, WIDTH - self.r)
        self.y = randint(self.r, HEIGHT - self.r)
        self.dx = choice([-5, -4, -3, 3, 4, 5])
        self.dy = choice([-5, -4, -3, 3, 4, 5])

        """
        self.color = "#%02x%02x%02x" % (randint(0, 255),
                                        randint(0, 255),
                                        randint(0, 255))
        """
        # self.w = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.w = tuple((randint(0, 255) for i in range(3)))
        self.color = "#%02x%02x%02x" % (self.w)
        self.ball_id = c.create_oval(self.x - self.r,
                                     self.y - self.r,
                                     self.x + self.r,
                                     self.y + self.r, fill=self.color)

    def move(self):

        # Прямолинейное движение
        self.x += self.dx
        self.y += self.dy

        # Столкновение шаров со стенами
        if self.x >= WIDTH - self.r or self.x <= self.r:
            self.dx = -self.dx
        if self.y >= HEIGHT - self.r or self.y <= self.r:
            self.dy = -self.dy

        # Столкновения шаров друг с другом
        # Берем массив всех шаров
        for another_ball in bs:
            # Удаляем из массива этот шар
            if another_ball.ball_id != self.ball_id:
                # определяем, что шар столкнулся с другим шаром
                if (self.x - another_ball.x) ** 2 + (self.y - another_ball.y) ** 2 <= (self.r + another_ball.r) ** 2:
                    self.dist = ((self.x - another_ball.x) ** 2 + (self.y - another_ball.y) ** 2)**0.5
                    # print(self.dist)
                    self.a = self.x - another_ball.x
                    self.b = self.y - another_ball.y
                    self.p1 = (self.a*self.b)/(self.dist**2)
                    self.p2 = (self.a/self.dist)**2
                    self.p3 = (self.b/self.dist)**2

                    self.d1 = self.dy*self.p1 + self.dx*self.p2 - another_ball.dy*self.p1 - another_ball.dx*self.p2
                    self.d2 = self.dx*self.p1 + self.dy*self.p3 - another_ball.dx*self.p1 - another_ball.dy*self.p3

                    self.dx = self.dx - self.d1
                    self.dy = self.dy - self.d2
                    another_ball.dx = another_ball.dx + self.d1
                    another_ball.dy = another_ball.dy + self.d2

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

    bs = [Ball() for i in range(2)]
    """
    bs = [
        Ball(50, 150, 500, 4, -5),
        Ball(50, 500, 500, -5, -4)
    ]
    """


    """
    bs = []
    for i in range(5):
        bs.append(Ball())
    """

    # print(math.degrees(calc_angle(4,3)))

    # print((bs))

    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
