def opener(file):
	with open(file) as fh:
		for line in fh:
			print(line.rstrip())

opener("alma.txt")