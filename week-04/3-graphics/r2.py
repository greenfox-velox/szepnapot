from tkinter import *


root = Tk()
canvas = Canvas(root, width='300', height='300', bg="white")

offset = 10

for i in range(15):
	canvas.create_line(150 - offset * i, 150, 150, 10 * i, fill="green")
	canvas.create_line(150 - offset * i, 150, 150, 300 - offset * i, fill="green")
	canvas.create_line(150 + offset * i, 150, 150, 10 * i, fill="green")
	canvas.create_line(150 + offset * i, 150, 150, 300 - offset * i, fill="green")
canvas.pack()
root.mainloop()