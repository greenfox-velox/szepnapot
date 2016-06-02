import sys, getopt
import csv

class ToDo:

	def __init__(self):
		try:
			self.loader('todo.csv')
		except FileNotFoundError:
			self.create()
		self.todo_list = self.get_list('todo.csv')
		self.completed = '[x]'
		self.incomplete = '[ ]'

	def usage(self):
		with open('usage.txt') as f:
			return f.read()

	def get_list(self, file):
		with open(file) as f:
			reader = csv.reader(f, delimiter=';')
			return list(map(tuple, reader))

	def list_view(self):
		content = self.get_list('todo.csv')
		formatted_content = []
		if len(content) < 1:
			return "No todos for today :)"
		for i in range(len(self.todo_list)):
			if self.todo_list[i][0] != 'True':
				formatted_content.append("{} - {} {}".format(str(i + 1), self.incomplete, self.todo_list[i][1]))
			else:
				formatted_content.append("{} - {} {}".format(str(i + 1), self.completed, self.todo_list[i][1]))
		return '\n'.join(formatted_content)


	def add_task(self, task):
		with open('todo.csv', 'a') as f:
			return f.write('{};{}'.format('False', str(task) + '\n'))

	def remove_task(self, task):
		try:
			self.todo_list.pop(int(task) - 1)
		except ValueError:
			print("Unable to remove: Index is out of bound")
		return self.save()


	def complete_task(self):
		
		pass

	def loader(self, file):
		with open(file) as f:
			return f.read()

	def save(self):
		with open('todo.csv', 'w') as f:
			for i in self.todo_list:
				f.write(i)

	def create(self):
		self.f = open('todo.txt', 'w')
		return self.f

t = ToDo()

def arguments(argv):
	try:
		opts, args = getopt.getopt(argv, "larc:d", ["list", "add", "remove", "complete"])
		if len(argv) < 1:
			print(t.usage())
	except getopt.GetoptError:
		print(t.usage())
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-l", "--list"):
			print(t.list_view())
		elif opt in ("-a", "--add"):
			try:
				t.add_task(args[0])
			except IndexError:
				print("Unable to add: No task is provided")
		elif opt in ("-r", "--remove"):
			try:
				t.remove_task(args[0])
			except IndexError:
				print("Unable to add: No task is provided")
		elif opt in ("-c", "--complete"):
			pass

if __name__ == '__main__':
	arguments(sys.argv[1:])