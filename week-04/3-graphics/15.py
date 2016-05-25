from tkinter import *

# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

def connect_points(lop):
	start_x = [x[0] for x in lop]
	start_y = [y[1] for y in lop]
	for i in range(len(start_x)):
			if i == len(start_x) - 1:
				canvas.create_line(start_x[i], start_y[i], start_x[0], start_y[0])
			else:
				canvas.create_line(start_x[i], start_y[i], start_x[i + 1], start_y[i + 1])



root = Tk()
canvas = Canvas(root, width='300', height='300')
connect_points([[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],[120, 100], [85, 130], [50, 100]])
canvas.pack()
root.mainloop()

