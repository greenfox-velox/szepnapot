from tkinter import *

# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.


class Example(Canvas):

	def __init__(self):
		Canvas.__init__(self)

	def draw_line(self, x, y):
		return canvas.create_line(x, y, x, y+50)

	def draw_square(self, x, y):
		return canvas.create_rectangle(x, y, x+50, y+50)

	def draw_square_middle(self, size):
		return canvas.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2)

if __name__ == '__main__':
	root = Tk()
	canvas = Canvas(root, width='300', height='300')
	E = Example()
	E.draw_square_middle(20)
	E.draw_square_middle(50)
	E.draw_square_middle(100)
	canvas.pack()
	root.mainloop()