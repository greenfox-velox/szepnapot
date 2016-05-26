from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300', bg="white")

def draw_pyramid(top_y=None, size=None):
	canvas.create_line(0, 300, 150, 75)
	canvas.create_line(300, 300, 150, 75)
	n = 0
	count = 1
	while n < 300:
		canvas.create_line(150 - size/2 * count, 75 + size, 150 + size/2 * count, 75 + size)
		n += size
		count += 1
draw_pyramid(size=20)
canvas.pack()
root.mainloop()