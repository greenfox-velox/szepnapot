class Person:

	def __init__(self, first="Tomi", last="Géza"):
		self.first = first
		self.last = last

	def greet(self):
		print("{} {}".format(self.first, self.last))


p = Person()
p.greet()