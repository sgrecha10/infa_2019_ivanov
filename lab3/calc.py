from tkinter import *
from tkinter import ttk


root = Tk()
root.title = 'Calc'
root.resizable(width=False, height=False)


display = ttk.Entry(root)
display.grid(row=0, column=0, columnspan=3)


buttons         = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
row_position    = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
column_position = [0, 1, 2, 0, 1, 2, 0, 1, 2, 1]

for id in range(0, len(buttons)):
    ttk.Button(root,
               text=buttons[id],
                command=lambda id=id: display.insert(0, buttons[id])).grid(row=row_position[id],
                column=column_position[id])

root.mainloop()