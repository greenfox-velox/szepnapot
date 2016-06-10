from tkinter import *
from tkinter import font
from map import Map
from hero import Hero


class Screen(object):

	def __init__(self, canvas):
		self.canvas = canvas
		self.hero = Hero()
		self.map = Map(self.hero, self.canvas)
		self.font_status = font.Font(size=12)
		self.font_game_over = font.Font(size=25)

	def is_hero_dead(self):
		return self.hero.current_hp <= 0

	def draw_map(self):
		if self.is_hero_dead():
			self.draw_end_screen()
		for i in self.map.map_texture:
			i.draw()
		self.draw_hero(self.hero.position['x'], self.hero.position['y'])
		self.draw_hero_status_bar()
		if self.map.is_valid_attack():
			self.draw_monster_status_bar(self.map.get_monster()[0])

	def draw_hero(self, x, y):
		self.canvas.create_image(x * 72, y * 72, image=self.hero.current_img, anchor=NW)

	def draw_hero_status_bar(self):
		self.canvas.delete("status")
		self.canvas.create_text(5, 722, text=self.hero, justify=CENTER, tags="status", anchor=NW, font=self.font_status)

	def draw_monster_status_bar(self, monster):
		self.canvas.create_text(500, 720, text=monster, tags="status", anchor=NW, font=self.font_status)

	def draw_end_screen(self):
		self.canvas.delete('all')
		self.canvas.create_text(300, 350, text="You died", anchor=NW, font=self.font_game_over, fill="red")