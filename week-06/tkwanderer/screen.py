from tkinter import *
from tkinter import font


class Screen(object):

	def __init__(self, canvas, map, hero):
		self.hero = hero
		self.map = map.map_texture
		self.canvas = canvas
		self.font = font.Font(size=15)

	def draw_map(self):
		for i in self.map:
			i.draw()
		self.draw_hero(self.hero.position['x'], self.hero.position['y'])
		self.draw_hero_status_bar()

	def draw_hero(self, x, y):
		self.canvas.create_image(x * 72, y * 72, image=self.hero.current_img, anchor=NW)

	def draw_hero_status_bar(self):
		self.canvas.delete("status")
		self.canvas.create_text(5, 720, text=self.hero, justify=CENTER, tags="status", anchor=NW, font=self.font)
