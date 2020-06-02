import tkinter as tk
import math
from random import randint, choice

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self):
        self.r = randint(50, 50)
        self.x = randint(self.r, WIDTH - self.r)
        self.y = randint(self.r, HEIGHT - self.r)
        self.dx = choice([-5, -4, -3, 3, 4, 5])
        self.dy = choice([-5, -4, -3, 3, 4, 5])
        # self.x = choice(200, 600)
        # self.y = 450
        # self.dx =

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

    def calc_angle(self, dx, dy):
        if self.dx > 0 and self.dy > 0:
            return math.atan(self.dy / self.dx) + 3 * math.pi / 2
        elif self.dx > 0 and self.dy < 0:
            return -(math.atan(self.dy / self.dx))
        elif self.dx < 0 and self.dy < 0:
            return math.atan(self.dy / self.dx) + math.pi / 2
        elif self.dx < 0 and self.dy > 0:
            return -(math.atan(self.dy / self.dx) - math.pi)
        elif self.dx == 0 and self.dy > 0:
            return 3 * math.pi / 2
        elif self.dx == 0 and self.dy < 0:
            return math.pi / 2
        elif self.dx > 0 and self.dy == 0:
            return 0
        elif self.dx < 0 and self.dy == 0:
            return math.pi
        else:
            return None

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
                    # print('self.x %s self.y %s self.dx %s self.dy %s' % (self.x, self.y, self.dx, self.dy))
                    # print("another_ball.x %s another_ball.y %s" % (another_ball.x, another_ball.y))
                    # рисуем векторы скоростей и сами скорости
                    c.create_line(self.x, self.y,
                                  (self.x + self.dx * 15), (self.y),
                                  fill="black", width=2, arrow=tk.LAST)
                    c.create_line(self.x, self.y,
                                  (self.x), (self.y + self.dy * 15),
                                  fill="black", width=2, arrow=tk.LAST)

                    c.create_line(another_ball.x, another_ball.y,
                                  (another_ball.x + another_ball.dx * 15), (another_ball.y),
                                  fill="black", width=2, arrow=tk.LAST)
                    c.create_line(another_ball.x, another_ball.y,
                                  (another_ball.x), (another_ball.y + another_ball.dy * 15),
                                  fill="black", width=2, arrow=tk.LAST)

                    c.create_line(self.x, self.y,
                                  (self.x + self.dx * 15), (self.y + self.dy * 15),
                                  fill="red", width=2, arrow=tk.LAST)
                    c.create_line(another_ball.x, another_ball.y,
                                  (another_ball.x + another_ball.dx * 15), (another_ball.y + another_ball.dy * 15),
                                  fill="green", width=2, arrow=tk.LAST)

                    # рисуем тонкую линию между центрами
                    c.create_line(self.x, self.y,
                                  another_ball.x, another_ball.y,
                                  fill="black", width=1)

                    # Определяем значение каждой скорости
                    self.v1 = (self.dx ** 2 + self.dy ** 2) ** 0.5
                    self.v2 = (another_ball.dx ** 2 + another_ball.dy ** 2) ** 0.5
                    #  print("self.v1 %s self.v2 %s" % (self.v1, self.v2))

                    # Определяем угол поворота оси относительно экранной системы координат
                    self.angleTheta = self.calc_angle(5, 5)
                    print("мы здесь", math.degrees(self.angleTheta))


                    """
                    # Определяем углы скоростей относительно экранной системы координат
                    if self.dx > 0 and self.dy > 0:
                        self.anglePhi1 = math.atan(self.dx / self.dy) + math.pi
                    elif self.dx > 0 and self.dy < 0:
                        self.anglePhi1 = math.atan(self.dx / self.dy)  # True
                    elif self.dx < 0 and self.dy > 0:
                        self.anglePhi1 = math.atan(self.dx / self.dy) + math.pi
                    elif self.dx < 0 and self.dy < 0:
                        self.anglePhi1 = math.atan(self.dx / self.dy)  # True

                    if another_ball.dx > 0 and another_ball.dy > 0:
                        self.anglePhi2 = math.atan(another_ball.dx / another_ball.dy) + math.pi
                    elif another_ball.dx > 0 and another_ball.dy < 0:
                        self.anglePhi2 = math.atan(another_ball.dx / another_ball.dy)  # True
                    elif another_ball.dx < 0 and another_ball.dy > 0:
                        self.anglePhi2 = math.atan(another_ball.dx / another_ball.dy) + math.pi
                    elif another_ball.dx < 0 and another_ball.dy < 0:
                        self.anglePhi2 = math.atan(another_ball.dx / another_ball.dy)  # True

                    # Проводим векторы скоростей через экранный угол
                    c.create_line(self.x, self.y,
                                  (self.x - self.v1 * 10 * math.sin(self.anglePhi1)),
                                  (self.y - self.v1 * 10 * math.cos(self.anglePhi1)),
                                  fill="blue", width=4, arrow=tk.LAST)

                    c.create_line(another_ball.x, another_ball.y,
                                  (another_ball.x - self.v2 * 10 * math.sin(self.anglePhi2)),
                                  (another_ball.y - self.v2 * 10 * math.cos(self.anglePhi2)),
                                  fill="blue", width=4, arrow=tk.LAST)

                    # Как провести линию определенной длины под определенным уголом из заданной точки (self.x, self.y)
                    """
                    """
                    self.angle = math.pi/2
                    self.vtest = 100
                    c.create_line(self.x, self.y,
                                  (self.x + self.vtest*math.cos(self.angle)), (self.y + self.vtest*math.sin(self.angle)),
                                  fill="black", width=1, arrow=tk.LAST)
                    """
                    """
                    # Определяем угол наклота оси столкновения
                    if (self.y - another_ball.y) > 0 and (self.x - another_ball.x) > 0:
                        self.Theta = math.atan((self.y - another_ball.y) / (self.x - another_ball.x)) + math.pi
                        print("1")
                    elif (self.y - another_ball.y) > 0 and (self.x - another_ball.x) < 0:
                        self.Theta = math.atan((self.y - another_ball.y) / (self.x - another_ball.x))  # True
                        print("2")
                    elif (self.y - another_ball.y) < 0 and (self.x - another_ball.x) > 0:
                        self.Theta = math.atan((self.y - another_ball.y) / (self.x - another_ball.x)) + math.pi  # True
                        print("3")
                    elif (self.y - another_ball.y) < 0 and (self.x - another_ball.x) < 0:
                        self.Theta = math.atan((self.y - another_ball.y) / (self.x - another_ball.x))  # True
                        print("4")

                    # Рисуем для проверки угла произвольную линию по углу между шарами
                    self.vtest = 300
                    c.create_line(self.x, self.y,
                                  (self.x + self.vtest * math.cos(self.Theta)),
                                  (self.y + self.vtest * math.sin(self.Theta)),
                                  fill="purple", width=4)

                    # Преобразовываем координаты скорости v2 в систему координат шаров
                    # self.new_v2 =
                    """

                    q = 1 / 0

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
