from character import Character

class Hero(Character):

	def __init__(self):
		super().__init__()
		self.position = {'x': 0, 'y': 0}
		self.current_img = self.hero_down_img
		self.hp = 20 + 3 + self.dice()
		self.dp = 2 * self.dice()
		self.sp = 5 + self.dice()
		self.current_hp = self.hp
		self.level = 1

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
		return "(HERO) LVL: {} | HP: {}/{} | DP: {} | SP: {}".format(self.level, self.hp, self.current_hp,
																																self.dp, self.sp)

	def get_strike(self, sp):
		return 2 * self.dice() + sp

	def attack(self, monster):
		hero_strike_value = self.sp + self.dice()*2
		monster_strike_value = monster.sp + self.dice()*2
		if self.get_strike(self.sp) > monster.dp:
			monster.hp -= hero_strike_value - monster.dp
		if self.get_strike(monster.sp) > self.dp:
			self.current_hp -= monster_strike_value - self.dp

	def level_up(self):
		self.level += 1
		self.hp += self.dice()
		self.dp += self.dice()
		self.sp += self.dice()
