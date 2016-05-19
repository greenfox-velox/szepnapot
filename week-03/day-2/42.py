lines_total = 0

with open('alma.txt') as alma:
	for line in alma:
		lines_total += 1

print("I've found",str(lines_total),"lines")