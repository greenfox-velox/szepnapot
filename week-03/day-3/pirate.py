class Pirate:

	def __init__(self):
		self.counter = 0

	def drink_rum(self):
		self.counter += 1

	def hows_goin_mate(self):
		if self.counter >= 5:
			print("Arrrrr!")
		else:
			print("Nothin'")

p = Pirate()
p.drink_rum()
p.drink_rum()
p.hows_goin_mate()