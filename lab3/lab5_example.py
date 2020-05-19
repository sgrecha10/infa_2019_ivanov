"""
Example from lecture 5
"""

from tkinter import *

import modul

def handler1(event):
    print("handler 1 worked. x = ", event.x, "y = ", event.y)


def handler2(event):
    exit()


# Инициализация
root = Tk()
#my_label = Label(root, text="My Label text")
#my_label.pack()


c = Canvas(root, width=400, height=300, bg='white')
c.pack()

c.create_oval(10, 10, 190, 190, fill='lightgrey', outline='white')
c.create_arc(10, 10, 190, 190, start=0, extent=45, fill='red')
c.create_arc(10, 10, 190, 190, start=180, extent=25, fill='orange')
c.create_arc(10, 10, 190, 190, start=240, extent=100, style=CHORD, fill='green')
c.create_arc(10, 10, 190, 190, start=160, extent=-70, style=ARC, outline='darkblue', width=5)

c.create_text(100, 100, text="Hello World,\nPython\nand Tk",
                justify=CENTER, font="Verdana 14")
c.create_text(200, 200, text="About this",
                anchor=NW, fill="grey")

my_button1 = Button(root, text="Кнопка 1").place(x=10, y=10, width=80)
my_button2 = Button(root, text="Кнопка 2").place(x=100, y=10, width=80)
my_button3 = Button(root, text="Кнопка 3").place(x=200, y=10, width=80)

# Привязка обработчика к событию и виджету
# виджет.bind(событие, обработчик)
#my_label.bind("<Button-1>", handler1)
#my_label.bind("<Button-3>", handler2)

print(__name__)

root.mainloop()
