from character import Character
from texture import Texture

class Skeleton(Character):

	def __init__(self, map_lvl, canvas, x, y):
		super().__init__()
		self.map_level = map_lvl
		self.texture = Texture(canvas, x, y)
		self.img = self.skeleton_img
		self.canvas = canvas
		self.position = (x, y)

		self.monster_hp = 2 * self.map_level * self.dice()
		self.monster_dp = self.map_level/2 * self.dice()
		self.monster_sp = self.map_level * self.dice()

	def draw(self):
		self.texture.draw_img(self.img)

	def __str__(self):
		return "HP: {}/{}, DP: {}, SP: {}".format(self.monster_hp, self.monster_hp,
																							self.monster_dp, self.monster_sp)
