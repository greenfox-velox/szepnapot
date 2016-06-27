from tkinter import *
from tkinter import font
import random
from map import Map
from hero import Hero
from skeleton import Skeleton


class Game(object):

	def __init__(self, canvas):
		self.canvas = canvas
		self.hero = Hero()
		self.map = Map(self.hero, self.canvas)
		self.font_status = font.Font(size=11)
		self.font_game_over = font.Font(size=25)

	def is_hero_dead(self):
		return self.hero.current_hp <= 0

	def is_monster_dead(self, monster):
		return monster.hp <= 0

	def is_boss_dead(self, monster):
		if monster.position == self.map.boss_position()[0].position:
			return self.is_monster_dead(monster)

	def combat(self):
		if self.is_hero_dead():
			self.canvas.delete('all')
			self.draw_end_screen()
		monster = self.map.get_monster()[0]
		self.hero.attack(monster)
		if self.is_boss_dead(monster):
			self.hero.level_up()
			self.new_level_buff()
			self.map.generate_level()
			self.hero.position = {'x': 0, 'y': 0}
			self.draw_map()
		if type(monster) == Skeleton:
			self.map.map_texture.remove(monster)
			self.hero.level_up()

	def random_chance(self):
		return random.randrange(0, 100)

	def new_level_buff(self):
		if self.random_chance() >= 90:
			self.hero.current_hp = self.hero.hp
		elif self.random_chance() >= 60:
			self.hero.current_hp += self.hero.current_hp // 3
			if self.hero.current_hp > self.hero.hp:
				self.hero.current_hp = self.hero.hp
		else:
			self.hero.current_hp += self.hero.current_hp // 10
			if self.hero.current_hp > self.hero.hp:
				self.hero.current_hp = self.hero.hp

	def move_route(self, key):
		# if self.hero.move_count == 2:
		# 	print("move")
		# 	self.map.move_monsters()
		# 	self.draw_map()
		# 	self.hero.move_count = 0
		pressed_key = key.keysym
		if pressed_key == 'Up':
			self.hero.move_up()
			if not self.map.is_valid_move():
				self.hero.move_down()
		elif pressed_key == 'Down':
			self.hero.move_down()
			if not self.map.is_valid_move():
				self.hero.move_up()
		elif pressed_key == 'Right':
			self.hero.move_right()
			if not self.map.is_valid_move():
				self.hero.move_left()
		elif pressed_key == 'Left':
			self.hero.move_left()
			if not self.map.is_valid_move():
				self.hero.move_right()
		elif pressed_key == 'space':
			if self.map.is_valid_move():
				self.combat()

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
		self.canvas.create_text(400, 722, text=monster, tags="status", anchor=NW, font=self.font_status, fill="red")

	def draw_end_screen(self):
		self.canvas.delete('all')
		self.canvas.create_text(300, 350, text="You died", anchor=NW, font=self.font_game_over, fill="red")