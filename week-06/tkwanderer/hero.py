from character import Character

class Hero(Character):

	def __init__(self):
		super().__init__()
		self.position = {'x': 0, 'y': 0}
		self.current_img = self.hero_down_img
		self.hero_max_hp = 20 + 3 + self.dice()
		self.hero_dp = 2 * self.dice()
		self.hero_sp = 5 + self.dice()
		self.current_hp = self.hero_max_hp

	def move_up(self):
		self.position['y'] -= 1
		self.current_img = self.hero_up_img

	def move_down(self):
		self.position['y'] += 1
		self.current_img = self.hero_down_img

	def move_right(self):
		self.position['x'] += 1
		self.current_img = self.hero_right_img

	def move_left(self):
		self.position['x'] -= 1
		self.current_img = self.hero_left_img

	def __str__(self):
		return "HP: {}/{} | DP: {} | SP: {}".format(self.hero_max_hp, self.current_hp,
																							self.hero_dp, self.hero_sp)
	# def attack(self):
	# 	return self.sp + self.d6 * 2
	#
	# def level_up(self):
	# 	self.hero_max_hp += self.d6
	# 	self.dp += self.d6
	# 	self.sp += self.d6
