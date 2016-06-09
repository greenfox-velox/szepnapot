import random

level_1_map = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
           		[0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
           		[0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
           		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           		[1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
           		[0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
           		[0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
           		[0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
           		[0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
           		[0, 0, 0, 1, 0, 1, 1, 0, 0, 0]]

def random_pos():
	return random.randint(0, 9)

def generate_monster_pos(count):
	m = 0
	while m <= 3:
		y = random_pos()
		x = random_pos()
		if level_1_map[y][x] != 1:
			level_1_map[y][x] = 3
			m += 1

generate_monster_pos(3)

print(level_1_map)

# map = []
# for i in range(len(level_1_map)):
# 	for e in range(len(level_1_map[i])):
# 		_row = {}
# 		_row['x'] = e
# 		_row['y'] = i
# 		if level_1_map[i][e] == 0:
# 			_row['type'] = 'tile'
# 		elif level_1_map[i][e]  == 1:
# 			_row['type'] = 'wall'
# 		elif level_1_map[i][e] == 2:
# 			_row['type'] = 'hero'
# 		map.append(_row)
