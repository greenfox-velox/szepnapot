from tkinter import PhotoImage

class Wall(object):

	def __init__(self, map):
		self.coord = map
		self.wall_img = PhotoImage(file='wall.png')
		self.position = self.coord.wall_positions()