"""
Example from lecture 5
"""

from tkinter import *


def handler1(event):
    print("handler 1 worked. x = ", event.x, "y = ", event.y)


def handler2(event):
    exit()


# Инициализация
root = Tk()
#my_label = Label(root, text="My Label text")
#my_label.pack()

my_button1 = Button(root, text="Кнопка 1").place(x=10, y=10, width=80)
my_button2 = Button(root, text="Кнопка 2").place(x=100, y=10, width=80)
my_button3 = Button(root, text="Кнопка 3").place(x=200, y=10, width=80)

# Привязка обработчика к событию и виджету
# виджет.bind(событие, обработчик)
#my_label.bind("<Button-1>", handler1)
#my_label.bind("<Button-3>", handler2)

root.mainloop()
