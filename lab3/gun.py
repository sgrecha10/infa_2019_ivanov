from random import randrange as rnd, choice
import tkinter as tk
import math
import time


# print (dir(math))


class Ball:
    def __init__(self, x=20, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 30
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30
        self.t = 1

    def set_coords(self):
        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.t += .3
        self.x += self.vx
        self.y -= self.vy - self.t ** 2

        """
        if self.x >= 800 or self.x <= 0:
            self.x = -self.x
        """

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME

        # print("Мяч:", self.x, self.y)
        # ("Мишень:", obj.x, obj.y, obj.r)

        if obj.x-obj.r-self.r < self.x < obj.x + obj.r+self.r \
                and obj.y+obj.r+self.r > self.y > obj.y-obj.r-self.r:
            canvas.delete(self.id)
            return True
        else:
            return False


class Gun:
    def __init__(self, x1=20, y1=450, x2=60, y2=410, width=7):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canvas.create_line(self.x1, self.y1, self.x2, self.y2, width=self.width)

    def fire2_start(self, event):
        self.f2_on = 1
        canvas.itemconfig(screen1, text='')

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        # new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - self.y1) / (event.x - self.x1))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')

        canvas.coords(self.id, self.x1, self.y1,
                      self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                      self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canvas.create_oval(0, 0, 0, 0)
        self.id_points = canvas.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = 30
        color = self.color = 'red'
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canvas.itemconfig(self.id_points, text=self.points)


"""
def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.move()
            b.set_coords()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)
"""


def init():
    global root, canvas, screen1, gun, target
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    screen1 = canvas.create_text(400, 300, text='', font='28')
    gun = Gun()
    target = Target()


def main():
    global balls, bullet, screen1, target, gun
    bullet = 0
    balls = []

    target.new_target()
    target.live = 1

    canvas.bind('<Button-1>', gun.fire2_start)
    canvas.bind('<ButtonRelease-1>', gun.fire2_end)
    canvas.bind('<Motion>', gun.targetting)
    # i = 0
    while target.live:
        # i += 1
        for b in balls:
            b.move()
            b.set_coords()
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()

                # canvas.bind('<Button-1>', '')
                # canvas.bind('<ButtonRelease-1>', '')
                canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')


        # print(i)
        canvas.update()
        time.sleep(0.03)
        gun.targetting()
        gun.power_up()
    # canvas.itemconfig(screen1, text='')
    canvas.delete(gun)
    print("мы тут")
    root.after(750, main)


if __name__ == "__main__":
    global root, canvas, gun, balls, bullet, target, screen1
    init()
    main()
    root.mainloop()
