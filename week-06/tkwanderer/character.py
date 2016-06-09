from tkinter import PhotoImage


class Character(object):

	def __init__(self, map):
		self.skeleton_img = PhotoImage(file='skeleton.png')
		self.hero_down_img = PhotoImage(file='hero-down.png')
		self.hero_up_img = PhotoImage(file='hero-up.png')
		self.hero_left_img = PhotoImage(file='hero-left.png')
		self.hero_right_img = PhotoImage(file='hero-right.png')
		self.boss_img = PhotoImage(file='boss.png')

		self.coord = map
