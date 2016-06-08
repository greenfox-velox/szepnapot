level_1_map = [[2, 0, 0, 1, 0, 1, 0, 0, 0, 0],
           		[0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
           		[0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
           		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           		[1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
           		[0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
           		[0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
           		[0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
           		[0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
           		[0, 0, 0, 1, 0, 1, 1, 0, 0, 0]]


map = []
for i in range(len(level_1_map)):
	for e in range(len(level_1_map[i])):
		_row = {}
		_row['x'] = e
		_row['y'] = i
		if level_1_map[i][e] == 0:
			_row['type'] = 'tile'
		elif level_1_map[i][e]  == 1:
			_row['type'] = 'wall'
		elif level_1_map[i][e] == 2:
			_row['type'] = 'hero'
		map.append(_row)
