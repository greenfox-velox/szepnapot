def opener(file):
	with open(file, 'w') as fh:
		for num in range(1, 11):
			fh.write(str(num) + "\n")

opener("alma.txt")