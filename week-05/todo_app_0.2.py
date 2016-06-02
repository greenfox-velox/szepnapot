import sys, getopt
from route import Routing

class ToDo:

	def __init__(self):
		try:
			self.loader('todo.txt')
		except FileNotFoundError:
			self.create()
		self.todo_list = self.get_list('todo.txt')

	def usage(self):
		with open('usage.txt') as f:
			return f.read()

	def get_list(self, file):
		with open(file) as f:
			return f.readlines()

	def list_view(self):
		content = self.get_list('todo.txt')
		if len(content) < 1:
			return "No todos for today :)"
		for i in range(len(content)):
			content[i] = '{} - '.format(str(i + 1)) + content[i]
		return ''.join(content)


	def add_task(self, task):
		with open('todo.txt', 'a') as f:
			return f.write(str(task) + "\n")

	def remove_task(self, task):
		try:
			self.todo_list.pop(int(task) - 1)
		except ValueError:
			print("Unable to remove: Index is out of bound")
		return self.save()


	def complete_task(self):
		# completes a task, put an 'X' to the end
		pass

	def loader(self, file):
		with open(file) as f:
			return f.read()

	def save(self):
		with open('todo.txt', 'w') as f:
			for i in self.todo_list:
				f.write(i)

	def create(self):
		self.f = open('todo.txt', 'w')
		return self.f

if __name__ == '__main__':
	r = Routing(sys.argv[1:])
	print(r.route())
