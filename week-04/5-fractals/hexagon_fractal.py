from tkinter import *
import math
import random

WIDTH = 800
HEIGHT = 800

root = Tk()

def gen_hex_colour_code():
   return '#' + ''.join([random.choice('0123456789ABCDEF') for x in range(6)])

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=gen_hex_colour_code())

def create_hex(topx, topy, size, fill=gen_hex_colour_code()):
  ma = math.sqrt(3) / 2 * size
  if size < 9:
    return
  canvas.create_polygon(topx, topy, topx + size, topy, topx + size + size/2, topy + ma, topx + size, topy + ma*2,
                        topx, topy + ma*2, topx - size/2, topy + ma, topx, topy, fill=fill, outline=fill)
  create_hex(topx, topy, size/3, fill=gen_hex_colour_code())
  create_hex(topx + size/3*2, topy, size / 3, fill=gen_hex_colour_code())
  create_hex(topx + size, 2/3 * ma + topy, size/3, fill=gen_hex_colour_code())
  create_hex(topx + size/3*2, topy + 4/3 * ma, size/3, fill=gen_hex_colour_code())
  create_hex(topx, topy + 4/3 * ma, size/3, fill=gen_hex_colour_code())
  create_hex(topx - size/3, 2/3 * ma + topy, size/3, fill=gen_hex_colour_code())


create_hex(300, 50, 300)
canvas.pack()
root.mainloop()