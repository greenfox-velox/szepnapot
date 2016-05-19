def opener(file):
	with open(file) as fh:
		for line in fh:
			print("A", line.rstrip())

opener("alma.txt")