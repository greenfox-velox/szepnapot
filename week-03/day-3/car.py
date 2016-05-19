class Car:

	def __init__(self, type="Porsche", km="10000"):
		self.type = type
		self.km = int(km)

	def ride(self, plus):
		self.km += int(plus)


c = Car("mazda", 12000)
c.ride(100)
print(c.type)
print(c.km)