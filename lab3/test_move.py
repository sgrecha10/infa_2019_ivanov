import tkinter as tk
import math


def calc_angle(ddx, ddy):
    if ddx > 0 and ddy > 0:
        return math.atan(ddy / ddx) + 3 * math.pi / 2
    elif ddx > 0 and ddy < 0:
        return -(math.atan(ddy / ddx))
    elif ddx < 0 and ddy < 0:
        return math.atan(ddy / ddx) + math.pi / 2
    elif ddx < 0 and ddy > 0:
        return -(math.atan(ddy / ddx) - math.pi)
    elif ddx == 0 and ddy > 0:
        return 3 * math.pi / 2
    elif ddx == 0 and ddy < 0:
        return math.pi / 2
    elif ddx > 0 and ddy == 0:
        return 0
    elif ddx < 0 and ddy == 0:
        return math.pi
    else:
        return None


def create_line_(angle, x0, y0, line):
    x1 = x0 - math.cos(angle) * line
    y1 = y0 - math.sin(angle) * line
    x2 = x0 + math.cos(angle) * line
    y2 = y0 + math.sin(angle) * line
    c.create_line(x1, y1, x2, y2, fill="black", width=1, arrow=tk.LAST)


root = tk.Tk()
c = tk.Canvas(root, width=800, height=600, bg="white")
c.pack()

# Нулевая координата новой системы координат (начало всех векторов), угол
x0 = 400
y0 = 300
anglePhi = math.radians(10)
print("Угол anglePhi: %.f гр." % math.degrees(anglePhi))
c.create_oval(x0-2, y0-2, x0+2, y0+2, fill="red")

# Рисуем новую систему координат
create_line_(anglePhi, x0, y0, 250)
create_line_(anglePhi + math.pi/2, x0, y0, 250)

# Рисуем произвольный вектор из центра координат, задавая координаты его второй точки
vx1 = 500
vy1 = 400
c.create_line(x0, y0, vx1, vy1, fill="blue", width=2, arrow=tk.LAST)

# Определяем новые координаты на новой системе отсчета и рисуем новый вектор
nx1 = vx1*math.cos(anglePhi) - vy1*math.sin(anglePhi)
ny1 = vx1*math.sin(anglePhi) + vy1*math.cos(anglePhi)
c.create_line(x0, y0, nx1, ny1, fill="green", width=2)

root.mainloop()