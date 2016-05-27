from tkinter import *
import math
import random

WIDTH = 800
HEIGHT = 800

root = Tk()

COLORS = ['red', 'orange red', 'tomato', 'dark orange', 'orange',
					'brown', 'firebrick', 'chocolate', 'wheat', 'beige', 'burlywood',
					'saddle brown', 'indian red', 'rosy brown', 'light goldenrod', 'gold',
					'yellow', 'yellow green', 'lime green', 'green yellow', 'green',
					'lawn green', 'spring green', 'sea green', 'aquamarine', 'turquoise',
					'light blue', 'deep sky blue', 'light slate blue', 'navy', 'deep pink',
					'orchid', 'purple']

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=random.choice(COLORS))

def triangle_pattern(x, y, size, fill=random.choice(COLORS)):
	ma = math.sqrt(3)/2 * size
	canvas.create_polygon([x, y, x + size, y, x + size / 2, y + ma],
												fill=fill, outline="black")
	if size <= 15:
		pass
	else:
		triangle_pattern(x, y, size / 2, fill=random.choice(COLORS))
		triangle_pattern(x + size / 2, y, size / 2, fill=random.choice(COLORS))
		triangle_pattern(x + size / 4, y + ma / 2, size / 2, fill=random.choice(COLORS))

triangle_pattern(50, 10, 700)

canvas.pack()
root.mainloop()