import csv

def add_task(task):
	with open('todo.csv', 'a') as f:
		return f.write('{};{}'.format('False', str(task) + '\n'))

def remove_task(task):
	try:
		del get_list('todo.csv')[int(task) - 1]
	except ValueError:
		print("Unable to remove: Index is out of bound")

def get_list(file):
	with open(file) as f:
		reader = csv.reader(f, delimiter=';')
		return list(map(tuple, reader))

completed = '[x]'
incomplete = '[ ]'

print(get_list('todo.csv'))
remove_task(2)
print(get_list('todo.csv'))

for i in range(len(your_list)):
	if your_list[i][0] != 'True':
		print("{} - {} {}".format(str(i + 1), completed, your_list[i][1]))
	else:
		print("{} - {} {}".format(str(i + 1), incomplete, your_list[i][1]))

