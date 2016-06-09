from character import Character
from texture import Texture

class Boss(Character):

	def __init__(self, map_lvl, canvas, x, y):
		super().__init__()
		self.map_level = map_lvl
		self.img = self.boss_img
		self.texture = Texture(canvas, x, y)
		self.canvas = canvas
		self.position = (x, y)

		self.boss_hp = 2 * self.map_level * self.dice() + self.dice()
		self.boss_dp = self.map_level/2 * self.dice() + self.dice()/2
		self.boss_sp = self.map_level * self.dice() + self.map_level

	def draw(self):
		self.texture.draw_img(self.img)

	def __str__(self):
		return "HP: {}/{}, DP: {}, SP: {}".format(self.boss_hp, self.boss_hp,
																							self.boss_dp, self.boss_sp)
