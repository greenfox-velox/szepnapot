from character import Character

class Boss(Character):

	def __init__(self, map):
		super().__init__(map)
		self.img = self.boss_img
		self.position = map.boss_position()