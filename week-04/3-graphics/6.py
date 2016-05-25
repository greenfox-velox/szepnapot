from tkinter import *

# create a 300x300 canvas.
# draw a green 10x10 square to its center.

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.create_rectangle(140, 140, 160, 160, fill="green")

root.mainloop()