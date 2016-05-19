class Person:

	def __init__(self, first="", last=""):
		self.first = first
		self.last = last

	def greet(self):
		print("{} {}".format(self.first, self.last))


class Student(Person):

	def __init__(self, grades=[], first="", last=""):
		super(Student, self).__init__(first="", last="")
		self.grades = grades
		self.first = first
		self.last = last

	def add_grades(self, grade):
		grade = int(grade)
		return self.grades.append(grade)

	def salute(self):
		average = sum(self.grades) / len(self.grades)
		print("{} {}, avarage: {}".format(self.first, self.last, average))


s = Student(first="Peter", last="Lodri")
s.add_grades(5)
s.add_grades(1)
s.add_grades(2)
s.add_grades(3)
s.salute()