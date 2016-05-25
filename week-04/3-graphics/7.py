from tkinter import *

# create a 300x300 canvas.
# fill it with four different size and color rectangles.

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

green_box = canvas.create_rectangle(240, 240, 160, 160, fill="green")
red_box = canvas.create_rectangle(100, 100, 160, 160, fill="red")
orange_box = canvas.create_rectangle(50, 50, 90, 90, fill="orange")
blue_box = canvas.create_rectangle(120, 160, 200, 200, fill="blue")


root.mainloop()