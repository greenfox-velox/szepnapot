from tkinter import *

WIDTH = 600
HEIGHT = 600

root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="yellow")

start_size = WIDTH/3

def draw_box(x, y, size):
	canvas.create_rectangle(x, y, x + size, y + size)

def pattern(start_x, start_y, size, level=0):
	if level == 5:
		return
	draw_box(start_x, start_y, size)
	draw_box(start_x + size, start_y + size, size)
	draw_box(start_x, start_y + size * 2, size)
	draw_box(start_x - size, start_y + size, size)
	pattern(start_x + size/3, start_y, size/3, level + 1)
	pattern(start_x + size/3 * 4, start_y + size, size / 3, level + 1)
	pattern(start_x + size/3, start_y + size * 2, size / 3, level + 1)
	pattern(start_x - size/3 * 2, start_y + size, size / 3, level + 1)

pattern(start_size, 0, start_size)

canvas.pack()
root.mainloop()

