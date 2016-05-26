from tkinter import *

# create a 300x300 canvas.
# fill it with a checkerboard pattern.


# def checkered(canvas, line_distance):
#    for x in range(line_distance, canvas_width, line_distance):
#       canvas.create_line(x, 0, x, canvas_height)
#    for y in range(line_distance, canvas_height, line_distance):
#       canvas.create_line(0, y, canvas_width, y)

root = Tk()
canvas_width = 300
canvas_height = 300
w = Canvas(root,
					 width=canvas_width,
					 height=canvas_height)

# for n in range(16):
# 	i = n % 4
# 	j = n // 4
# 	ox = 20 + i
# 	oy = 20 + j
# 	w.create_rectangle(0 + ox, 0 + oy, 20 + ox, 20 + oy, fill="white")
# 	w.create_rectangle(20 + ox, 20 + oy, 40 + ox, 40 + oy, fill="white")
w.pack()
mainloop()
