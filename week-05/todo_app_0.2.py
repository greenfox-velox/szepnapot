import sys
import csv
from route import Parser

class Controller(Parser):

	def __init__(self):
		super().__init__(sys.argv[1:])
		self.fh = FileHandling('todo.csv')
		self.todo = ToDo(self.fh.list_from_csv())
		self.menu = {'-l': self.view(), '-a': self.add(),
								 '-r': self.remove(), '-c': self.complete()}

	def route(self):
		return self.menu[self.opt]

	def view(self):
		formatted_content = []
		if len(self.todo.todo_list) < 1:
			return "No todos for today :)"
		for i in range(len(self.todo.todo_list)):
			if self.todo.todo_list[i][0] != 'True':
				formatted_content.append("{} - {} {}".format(str(i + 1), self.todo.incomplete, self.todo.todo_list[i][1]))
			else:
				formatted_content.append("{} - {} {}".format(str(i + 1), self.todo.completed, self.todo.todo_list[i][1]))
		sys.stderr.write('\n'.join(formatted_content))

	def add(self):
		self.todo.add_task(self.passed_arg)
		self.fh.save_to_file(self.todo.todo_list)

	def remove(self):
		self.todo.remove_task(self.passed_arg)
		self.fh.save_to_file(self.todo.todo_list)

	def complete(self):
		self.todo.complete_task(self.passed_arg)
		self.fh.save_to_file(self.todo.todo_list)

class FileHandling:

	def __init__(self, file_name):
		self.file = file_name
		try:
			open(self.file)
		except FileNotFoundError:
			self.create_csv()

	def list_from_csv(self):
		with open(self.file) as f:
			reader = csv.reader(f, delimiter=';')
			self.csvlist = list(reader)
		return self.csvlist

	def save_to_file(self, list_to_write):
		with open(self.file, 'w', newline='') as f:
			todo_writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			for line in list_to_write:
				todo_writer.writerow(line)

	def create_csv(self):
		create_file = open(self.file, 'w')
		create_file.close()

class ToDo:

	def __init__(self, todo_list):
		self.todo_list = todo_list
		self.completed = '[x]'
		self.incomplete = '[ ]'

	def add_task(self, task):
		self.todo_list.append(['False', task])

	def remove_task(self, task):
		try:
			self.todo_list.pop(int(task) - 1)
		except ValueError:
			return "Unable to remove: Index is out of bound"

	def complete_task(self, task):
		try:
			self.todo_list[int(task) - 1][0] = 'True'
		except TypeError:
			return "Unable to check: Index is not a number"
		except IndexError:
			return "Unable to check: Index is out of bound"

c = Controller()
