from character import Character
from texture import Texture

class Skeleton(Character):

	def __init__(self, map_lvl, canvas, x, y):
		super().__init__()
		self.map_level = map_lvl
		self.texture = Texture(canvas, x, y)
		self.img = self.skeleton_img
		self.canvas = canvas
		self.position = {'x': x, 'y': y}

		self.hp = 2 * self.map_level * self.dice()
		self.dp = self.map_level/2 * self.dice()
		self.sp = self.map_level * self.dice()

	def draw(self):
		self.texture.draw_img(self.img)

	def __str__(self):
		return "(SKELETON) HP: {} | DP: {} | SP: {}".format(self.hp,
																							self.dp, self.sp)
