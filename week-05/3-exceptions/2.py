# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def file_reader(file):
	try:
		with open(file) as f:
			return len(f.readlines())
	except FileNotFoundError:
		return 0

print(file_reader("open.txt"))