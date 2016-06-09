from tkinter import PhotoImage
import random

class Character(object):

	def __init__(self):
		self.skeleton_img = PhotoImage(file='skeleton.png')
		self.hero_down_img = PhotoImage(file='hero-down.png')
		self.hero_up_img = PhotoImage(file='hero-up.png')
		self.hero_left_img = PhotoImage(file='hero-left.png')
		self.hero_right_img = PhotoImage(file='hero-right.png')
		self.boss_img = PhotoImage(file='boss.png')

	def dice(self):
		return random.randint(1, 6)

	# def attack(self, position):
	# 	hero_strike_value = self. + self.dice()*2

