import random
from wall import Wall
from character import Character

class Hero(Character):

	def __init__(self, map):
		super().__init__(map)
		self.wall = Wall(map)
		self.coord = map
		self.position = {'x': 0, 'y': 0}
		self.current_img = self.hero_down_img
		self.d6 = random.randint(1, 6)
		self.max_hp = 20 + 3 * self.d6
		self.dp = 2 * self.d6
		self.sp = 5 + self.d6

	def move_route(self, key):
		direction = key.keysym

		if direction == 'Up':
			self.move_up()
			if not self.is_valid_move():
				self.move_down()

		elif direction == 'Down':
			self.move_down()
			if not self.is_valid_move():
				self.move_up()

		elif direction == 'Right':
			self.move_right()
			if not self.is_valid_move():
				self.move_left()

		elif direction == 'Left':
			self.move_left()
			if not self.is_valid_move():
				self.move_right()

	def is_valid_move(self):
		if (self.position['x'], self.position['y']) in self.wall.position:
			return False
		if self.position['x'] not in list(range(10)):
			return False
		if self.position['y'] not in list(range(10)):
			return False
		return True

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
		return "HP: {}/{}, DP: {}, SP: {}".format(self.max_hp, self.max_hp,
																							self.dp, self.sp)
	def attack(self):
		return self.sp + self.d6 * 2

	def level_up(self):
		self.max_hp += self.d6
		self.dp += self.d6
		self.sp += self.d6
