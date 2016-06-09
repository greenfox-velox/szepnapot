from tkinter import PhotoImage
from map import Map

class Tile(object):

	def __init__(self, map):
		self.coord = map
		self.tile_img = PhotoImage(file='floor.png')
		self.position = self.coord.tile_positions()