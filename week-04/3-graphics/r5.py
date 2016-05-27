from tkinter import *

root = Tk()

WIDTH = 600
HEIGHT = 600
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")

def triangle(topx, topy, leftx, lefty, rightx, righty):
	canvas.create_line(topx, topy, leftx, lefty)
	canvas.create_line(leftx, lefty, rightx, righty)
	canvas.create_line(rightx, righty, topx, topy)

def pattern(topx, topy, leftx, down_y, rightx, size):
	if topy + size > down_y:
		return
	triangle(topx, topy, leftx, down_y, rightx, down_y)
	pattern(topx, topy + 20, leftx + size, down_y - size/2, rightx - size, size)


pattern(WIDTH/2, 100, 0, 500, WIDTH, 20)

canvas.pack()
root.mainloop()