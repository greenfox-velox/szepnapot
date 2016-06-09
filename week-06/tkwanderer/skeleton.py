from character import Character

class Skeleton(Character):

	def __init__(self, map):
		super().__init__(map)
		self.img = self.skeleton_img
		self.position = map.monster_positions()