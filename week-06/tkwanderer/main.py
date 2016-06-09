from tkinter import *
from screen import Screen
from hero import Hero
from map import Map

WIDTH = 720
HEIGHT = 740

def main():
	root = Tk()
	canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
	m = Map()
	h = Hero(m)
	s = Screen(canvas, m, h)
	s.draw_map()
	def move(event):
		h.move_route(event)
		s.draw_map()
	canvas.bind("<Key>", move)
	canvas.pack()
	canvas.focus_set()
	root.mainloop()

main()