from tkinter import *

# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.


class Example(Canvas):

	def __init__(self):
		Canvas.__init__(self)

	def draw_line(self, x, y):
		return canvas.create_line(x, y, x, y+50)

	def draw_square(self, x, y):
		return canvas.create_rectangle(x, y, x+50, y+50)

if __name__ == '__main__':
	root = Tk()
	canvas = Canvas(root, width='300', height='300')
	E = Example()
	E.draw_square(100, 50)
	E.draw_square(20, 75)
	E.draw_square(230, 100)
	canvas.pack()
	root.mainloop()