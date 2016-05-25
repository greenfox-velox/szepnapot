from tkinter import *

# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.


class Example(Canvas):

	def __init__(self):
		Canvas.__init__(self)

	def draw_line(self, x, y):
		return canvas.create_line(x, y, x, y+50)

	def draw_square(self, x, y):
		return canvas.create_rectangle(x, y, x+50, y+50)

	def draw_square_middle(self, size, color='red'):
		return canvas.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2, fill=color)

	def paused_line_middle(self, x, y, line=20, space=20):
		return canvas.create_line(x, y, 150, 150, dash=(line, space))


if __name__ == '__main__':
	root = Tk()
	canvas = Canvas(root, width='300', height='300')
	E = Example()
	E.paused_line_middle(0, 0)
	E.paused_line_middle(300, 0)
	E.paused_line_middle(0, 300)
	E.paused_line_middle(300, 300)
	canvas.pack()
	root.mainloop()


