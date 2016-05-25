from tkinter import *

# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

COLORS = ['red', 'orange red', 'tomato', 'dark orange', 'orange',
					'brown', 'firebrick', 'chocolate', 'wheat', 'beige', 'burlywood',
					'saddle brown', 'indian red', 'rosy brown', 'light goldenrod', 'gold',
					'yellow', 'yellow green', 'lime green', 'green yellow', 'green',
					'lawn green', 'spring green', 'sea green', 'aquamarine', 'turquoise',
					'light blue', 'deep sky blue', 'light slate blue', 'navy', 'deep pink',
					'orchid', 'purple']


class Example(Canvas):

	def __init__(self):
		Canvas.__init__(self)

	def draw_line(self, x, y):
		return canvas.create_line(x, y, x, y+50)

	def draw_square(self, x, y):
		return canvas.create_rectangle(x, y, x+50, y+50)

	def draw_square_middle(self, size, color='red'):
		return canvas.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2, fill=color)

size = 300

if __name__ == '__main__':
	root = Tk()
	canvas_width = 300
	canvas_height = 300
	canvas = Canvas(root, width=canvas_width, height=canvas_height)
	E = Example()
	for col in COLORS:
		E.draw_square_middle(size, color=col)
		size -= 10
	canvas.pack()
	root.mainloop()