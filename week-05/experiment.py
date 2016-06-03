import csv

# def add_task(task):
# 	with open('todo.csv', 'a') as f:
# 		return f.write('{};{}'.format('False', str(task) + '\n'))
#
# def remove_task(task):
# 	try:
# 		del get_list('todo.csv')[int(task) - 1]
# 	except ValueError:
# 		print("Unable to remove: Index is out of bound")

def get_list(file):
	with open(file) as f:
		reader = csv.reader(f, delimiter=';')
		return list(reader)

lista = get_list('todo.csv')
lista.append(['False','coffee'])
print(lista)

# def complete_task(task):
# 	try:
# 		get_list('todo.csv')[int(task) - 1] = 'True'
# 	except ValueError:
# 		print("Unable to remove: Index is out of bound")
# 	return

# print(get_list('todo.csv'))

# lista = [['False', 'Eat'], ['False', 'Sleep'], ['True', 'Shop'], ['False', 'Drink'], ['False', 'Food']]
#
# with open('todo.csv', 'w', newline='') as f:
# 	spamwriter = csv.writer(f, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	for line in lista:
# 		spamwriter.writerow(line)


