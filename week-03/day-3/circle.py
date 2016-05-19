import math

class Circle:
	"""Calculate area, and circumference
	for given radius"""

	def __init__(self, radius):
		self.radius = radius

	def get_circumference(self):
		return math.pi * 2 * self.radius

	def get_area(self):
		return math.pi * self.radius**2


radius = int(input("Enter radius: "))

c = Circle(radius)
print("Circumference:",c.get_circumference())
print("Area:",c.get_area())