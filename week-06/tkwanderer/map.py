import random

class Map:

	def __init__(self):
		self.gen_map()
		self.generate_monster_pos(3)
		self.generate_boss_pos()
		self.get_map_dict()

	def gen_map(self):
		self.map = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
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

	def random_pos(self):
		return random.randint(0, 9)

	def generate_monster_pos(self, count):
		m = 0
		while m < 3:
			y = self.random_pos()
			x = self.random_pos()
			if y == 0 and x == 0:
				y = self.random_pos()
				x = self.random_pos()
			if self.map[y][x] == 0:
				self.map[y][x] = 3
				m += 1

	def generate_boss_pos(self):
		b = 0
		while b == 0:
			y = self.random_pos()
			x = self.random_pos()
			if y == 0 and x == 0:
				y = self.random_pos()
				x = self.random_pos()
				continue
			if self.map[y][x] == 0:
				self.map[y][x] = 4
				b += 1

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
				elif self.map[i][e] == 3:
					_row['type'] = 'skeleton'
				elif self.map[i][e] == 4:
					_row['type'] = 'boss'
				self.map_dict.append(_row)
		return self.map_dict

	def wall_positions(self):
		return [(i['x'], i['y']) for i in self.map_dict if i['type'] == 'wall']

	def tile_positions(self):
		return [(i['x'], i['y']) for i in self.map_dict if i['type'] == 'tile']

	def monster_positions(self):
		return [(i['x'], i['y']) for i in self.map_dict if i['type'] == 'skeleton']

	def boss_position(self):
		return [(i['x'], i['y']) for i in self.map_dict if i['type'] == 'boss']