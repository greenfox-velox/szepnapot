from tkinter import *
from wall import Wall
from tile import Tile
from skeleton import Skeleton
from boss import Boss

class Screen(object):

	def __init__(self, canvas, map, hero):
		self.wall = Wall(map)
		self.tile = Tile(map)
		self.skeleton = Skeleton(map)
		self.boss = Boss(map)
		self.hero = hero
		self.coords = map
		self.canvas = canvas

	def draw_map(self):
		for i in self.tile.position:
			self.draw_tile(i[0] * 72, i[1] * 72)
		for i in self.wall.position:
			self.draw_wall(i[0] * 72, i[1] * 72)
		for i in self.skeleton.position:
			self.draw_monster(i[0] * 72, i[1] * 72)
		self.draw_boss(self.boss.position[0][0] * 72, self.boss.position[0][1] * 72)
		self.draw_hero(self.hero.position['x'] * 72, self.hero.position['y'] * 72, self.hero.current_img)
		self.draw_status_bar()

	def draw_wall(self, x, y):
		self.canvas.create_image(x, y, image=self.wall.wall_img, anchor=NW)

	def draw_tile(self, x, y):
		self.canvas.create_image(x, y, image=self.tile.tile_img, anchor=NW)

	def draw_hero(self, x, y, direction):
		self.canvas.create_image(x, y, image=direction, anchor=NW)

	def draw_monster(self, x, y):
		self.draw_tile(x, y)
		self.canvas.create_image(x, y, image=self.skeleton.img, anchor=NW)

	def draw_boss(self, x, y):
		self.draw_tile(x, y)
		self.canvas.create_image(x, y, image=self.boss.img, anchor=NW)

	def draw_status_bar(self):
		self.canvas.delete("status")
		self.canvas.create_text(300, 730, text=self.hero, justify=CENTER, tags="status")