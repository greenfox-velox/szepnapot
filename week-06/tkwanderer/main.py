from tkinter import *
from game import Game

WIDTH = 720
HEIGHT = 740

def main():
	root = Tk()
	canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
	s = Game(canvas)
	s.draw_map()

	def move(event):
		s.move_route(event)
		canvas.delete('all')
		s.draw_map()

	canvas.bind("<Key>", move)
	canvas.pack()
	canvas.focus_set()
	root.mainloop()

main()