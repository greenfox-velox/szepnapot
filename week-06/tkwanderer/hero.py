from dice import Dice

class Hero(Dice):

	def __init__(self):
		self.max_hp = 20 + 3 * self.d6()
		self.dp = 2 * self.d6()
		self.sp = 5 + self.d6()

	def __str__(self):
		return "HP: {}/{}, DP: {}, SP: {}".format(self.max_hp, self.max_hp,
																							self.dp, self.sp)

	def attack(self):
		return self.sp + self.d6() * 2

	def level_up(self):
		self.max_hp += self.d6()
		self.dp += self.d6()
		self.sp += self.d6()
