class Student:

	def __init__(self, grades=[]):
		self.grades = grades


	def add_grade(self, grade):
		if grade > 5:
			print("Invalid grade, {}".format(grade))
		else:
			self.grades.append(grade)

	def get_average(self):
		return sum(self.grades) / len(self.grades)


s = Student()
s.add_grade(6)
s.add_grade(4)
s.add_grade(1)
s.add_grade(3)
print(s.get_average())
