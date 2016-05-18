def linear_search(lista=[4, 5, 6], num=6):
	if num not in lista:
		print(-1)
	for i in lista:
		if i == num:
			print(lista.index(i))
			break
		else:
			continue

linear_search(num=47)