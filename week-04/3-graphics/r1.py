from tkinter import *

def weird_lines_left(color=None,y_focus=None, x_focus=None, offset=None):
	current_x = 0
	while current_x < x_focus[1]:
		canvas.create_line(current_x, 300, 0, y_focus[1] + current_x, fill=color)
		current_x += offset

def weird_lines_right(color=None,y_focus=None, x_focus=None, offset=None):
	current_x = 300 - offset
	while current_x > x_focus[1]:
		canvas.create_line(current_x, 0, y_focus[0], current_x, fill=color)
		current_x -= offset



root = Tk()
canvas = Canvas(root, width='300', height='300', bg="white")
weird_lines_left(y_focus=(0, 25), x_focus=(150, 300), offset=20, color="green")
weird_lines_right(y_focus=(300, 275), x_focus=(150, 0), offset=20, color="purple")
canvas.pack()
root.mainloop()