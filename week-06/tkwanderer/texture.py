from tkinter import *

class Texture(object):

	def __init__(self, canvas, x, y):
		self.row = x
		self.column = y
		self.canvas = canvas
		self.size = 72
		self.position = {'x': x, 'y': y}

	def draw_img(self, picture):
		self.canvas.create_image(1 + self.row * self.size, 1 + self.column * self.size, image=picture, anchor=NW)

class Wall(Texture):

	def __init__(self, canvas, x, y):
		super().__init__(canvas, x, y)
		self.wall_img = PhotoImage(file='wall.png')

	def draw(self):
		self.draw_img(self.wall_img)

class Tile(Texture):

	def __init__(self, canvas, x, y):
		super().__init__(canvas, x, y)
		self.tile_img = PhotoImage(file='floor.png')

	def draw(self):
		self.draw_img(self.tile_img)