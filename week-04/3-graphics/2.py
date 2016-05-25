from tkinter import *

# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

orange_line = canvas.create_line(25, 10, 25, 160, fill='orange')
red_line = canvas.create_line(25, 10, 175, 10, fill='red')
green_line = canvas.create_line(175, 10, 175, 160, fill='green')
blue_line = canvas.create_line(25, 160, 175, 160, fill='blue')

root.mainloop()