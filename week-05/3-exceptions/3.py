# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person:

	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate
		print(self.validate())

	def validate(self):
		try:
			if 0 < self.birthdate < 2016:
				return "{} was born in {}.".format(self.name, self.birthdate)
			raise ValueError
		except ValueError:
			return "Invalid birthdate: {}".format(self.birthdate)

p = Person(name="Peter", birthdate=1992)
pe = Person(name="Peter", birthdate=0)
