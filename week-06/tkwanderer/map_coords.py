class Coordinates:

	def __init__(self):
		self.floor = 0
		self.wall = 1
		self.hero = 2
		self.monster = 3
		self.boss = 4
		self.gen_map()
		self.get_map_dict()

	def gen_map(self):
		self.map = [[2, 0, 0, 1, 0, 1, 0, 0, 0, 0],
									 [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
									 [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
									 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
									 [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
									 [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
									 [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
									 [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
									 [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
									 [0, 0, 0, 1, 0, 1, 1, 0, 0, 0]]
		return self.map

	def get_map_dict(self):
		self.map_dict = []
		for i in range(len(self.map)):
			for e in range(len(self.map[i])):
				_row = {}
				_row['x'] = e
				_row['y'] = i
				if self.map[i][e] == 0:
					_row['type'] = 'tile'
				elif self.map[i][e] == 1:
					_row['type'] = 'wall'
				elif self.map[i][e] == 2:
					_row['type'] = 'hero'
				self.map_dict.append(_row)
		return self.map_dict

	def hero_position(self):
		return [i for i in self.map_dict if i['type'] == 'hero']

	def wall_positions(self):
		return [(i['x'], i['y']) for i in self.map_dict if i['type'] == 'wall']

	def monster_positions(self):
		pass