def forest(ac, time):
	if ac % 4 == 0:
		if time <= 200:
			print('Check')
		else:
			print('Time Out')
	else:
		print('Run Forest Run!')


forest(8, 120)
forest(8, 201)
