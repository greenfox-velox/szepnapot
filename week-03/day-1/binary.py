def listaSort(lista):
	data_list = lista
	new_list = []

	while data_list:
		minimum = data_list[0]
		for x in data_list:
			if x < minimum:
				minimum = x
		new_list.append(minimum)
		data_list.remove(minimum)
	return new_list

def binary_search(lista, num):
	search = listaSort(lista)
	lower = 0
	upper = len(search)
	while lower < upper:
		x = lower + (upper - lower) // 2
		val = search[x]
		if num == val:
			return x, True
		elif num > val:
			if lower == x:
				break
			lower = x
		elif num < val:
			upper = x
	return False


print(binary_search([1, 2, 3, 4, 7], 9))