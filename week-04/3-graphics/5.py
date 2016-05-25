from tkinter import *

# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.


class Example(Canvas):

	def __init__(self):
		Canvas.__init__(self)

	def draw_line(self, x, y):
		return canvas.create_line(x, y, x, y+50)


if __name__ == '__main__':
	root = Tk()
	canvas = Canvas(root, width='300', height='300')
	E = Example()
	E.draw_line(100, 50)
	E.draw_line(20, 75)
	E.draw_line(230, 100)
	canvas.pack()
	root.mainloop()
