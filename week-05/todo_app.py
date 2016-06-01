import sys, getopt

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
		self.todo_list.pop(int(task) - 1)
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
