from tkinter import *


def diagonal_squares(x, y, size, boxes, grow=False):
	start_x = x
	start_y = y
	for i in range(1, boxes + 1):
		if grow:
			end_x = start_x + size * i
			end_y = start_y + size * i
		else:
			end_x = start_x + size
			end_y = start_y + size
		canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="purple")
		start_x = end_x
		start_y = end_y


root = Tk()
canvas = Canvas(root, width='300', height='300')
diagonal_squares(50, 50, 10, 5)
# diagonal_squares(50, 50, 10, 5, grow=True)
canvas.pack()
root.mainloop()
