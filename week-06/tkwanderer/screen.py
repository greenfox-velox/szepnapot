from img_store import Textures
from map_coords import Coordinates
from tkinter import *

class Screen(object):

	def __init__(self, canvas):
		self.textures = Textures()
		self.coords = Coordinates()
		self.canvas = canvas

	def draw_map(self):
		for i in self.coords.map_dict:
			if i['type'] == 'tile':
				self.draw_tile(i['x'] * 72, i['y'] * 72)
			if i['type'] == 'wall':
				self.draw_wall(i['x'] * 72, i['y'] * 72)
		for i in self.coords.map_dict:
			if i['type'] == 'hero':
				self.draw_hero(i['x'] * 72, i['y'] * 72)

	def draw_wall(self, x, y):
		self.canvas.create_image(x, y, image=self.textures.wall, anchor=NW)

	def draw_tile(self, x, y):
		self.canvas.create_image(x, y, image=self.textures.floor, anchor=NW)

	def draw_hero(self, x, y):
		self.draw_tile(x, y)
		self.canvas.create_image(x, y, image=self.textures.hero_down, anchor=NW)
