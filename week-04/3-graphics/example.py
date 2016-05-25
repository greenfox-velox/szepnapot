from tkinter import Canvas


class Example(Canvas):

	def __init__(self):
		Canvas.__init__(self)

	def draw_line(self, x, y):
		return self.create_line(x, y, x, y+50)

	def draw_square(self, x, y):
		return self.create_rectangle(x, y, x+50, y+50)

	def draw_square_middle(self, size, color='red'):
		return self.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2, fill=color)

	def paused_line_middle(self, x, y, line=20, space=20):
		return self.create_line(x, y, 150, 150, dash=(line, space))

	def diagonal_squares(self, x, y, size, boxes):
		for i in range(1, boxes + 1):
			return self.create_rectangle(x, y, x + size * i, y + size * i)

