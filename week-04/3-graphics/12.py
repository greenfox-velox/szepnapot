from tkinter import *

# create a 300x300 canvas.
# fill it with a checkerboard pattern.


def checkered(canvas, line_distance):
   for x in range(line_distance, canvas_width, line_distance):
      canvas.create_line(x, 0, x, canvas_height)
   for y in range(line_distance, canvas_height, line_distance):
      canvas.create_line(0, y, canvas_width, y)


root = Tk()
canvas_width = 300
canvas_height = 300
w = Canvas(root,
           width=canvas_width,
           height=canvas_height)
w.pack()
checkered(w, 20)
mainloop()
