from tkinter import *
import random

# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

root = Tk()
canvas = Canvas(root, width='300', height='300', bg="black")

grays = [
	'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
	'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
	'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
	'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99'
				 ]


def create_star():
	start_x = random.randint(5, 300)
	start_y = random.randint(5, 300)
	if start_y == start_x:
		start_y = random.randint(5, 300)
	canvas.create_rectangle(start_x, start_y, start_x+20, start_y+20, fill=random.choice(grays))


# def create_star(x, y, size=20):
# 	canvas.create_line(start_x, start_y, start_x + size/2, start_y + size/2, color=random.choice(grays))
# 	canvas.create_line(start_x + size/2, start_y + size/2, start_x, start_y + size, color=random.choice(grays))
# 	canvas.create_line(start_x, start_y + size, start_x - size/2, start_y + size/2, color=random.choice(grays))
# 	canvas.create_line(start_x - size/2, start_y + size/2, start_x, start_y, color=random.choice(grays))

def create_sky(stars):
	for i in range(stars):
		create_star()

create_sky(50)

canvas.pack()
root.mainloop()