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

def draw_hex():
	pass


def create_hex(topx, topy, size, fill=random.choice(COLORS)):
	ma = math.sqrt(3) / 2 * size
	if size < 9:
		return
	canvas.create_polygon(topx, topy, topx + size, topy, topx + size + size/2, topy + ma, topx + size, topy + ma*2,
												topx, topy + ma*2, topx - size/2, topy + ma, topx, topy, fill=fill, outline="black")
	create_hex(topx, topy, size/3, fill=random.choice(COLORS))
	create_hex(topx + size/3*2, topy, size / 3, fill=random.choice(COLORS))
	create_hex(topx + size, 2/3 * ma + topy, size/3, fill=random.choice(COLORS))
	create_hex(topx + size/3*2, topy + 4/3 * ma, size/3, fill=random.choice(COLORS))
	create_hex(topx, topy + 4/3 * ma, size/3, fill=random.choice(COLORS))
	create_hex(topx - size/3, 2/3 * ma + topy, size/3, fill=random.choice(COLORS))


create_hex(300, 50, 300)
canvas.pack()
root.mainloop()