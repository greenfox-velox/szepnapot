from tkinter import *
from movement import Move

WIDTH = 720
HEIGHT = 720

def main():
	root = Tk()
	canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
	m = Move(canvas)
	m.screen.draw_map()
	def move(event):
		m.route(event)
		m.screen.draw_map()
	canvas.bind("<Key>", move)
	canvas.pack()
	print(m.screen.coords.get_map_dict())
	canvas.focus_set()
	root.mainloop()

main()