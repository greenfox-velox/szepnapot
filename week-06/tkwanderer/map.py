import random
from texture import Wall, Tile
from skeleton import Skeleton
from boss import Boss

class Map:

	def __init__(self, hero, canvas):
		self.canvas = canvas
		self.map_level = 0
		self.generate_level()
		self.hero = hero

	def generate_level(self):
		self.map_level += 1
		self.gen_map()
		self.generate_monster_pos(self.get_monster_quantity())
		self.generate_boss_pos()
		self.make_map_texture()

	def gen_map(self):
		self.raw_map = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
									 [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
									 [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
									 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
									 [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
									 [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
									 [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
									 [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
									 [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
									 [0, 0, 0, 1, 0, 1, 1, 0, 0, 0]]
		return self.raw_map

	def random_pos(self):
		return random.randint(0, 9)

	def get_monster_quantity(self):
		return random.randint(3, 5)

	def generate_monster_pos(self, count):
		m = 0
		while m < count:
			y = self.random_pos()
			x = self.random_pos()
			if y == 0 and x == 0:
				y = self.random_pos()
				x = self.random_pos()
			if self.raw_map[y][x] == 0:
				self.raw_map[y][x] = 3
				m += 1

	def generate_boss_pos(self):
		b = 0
		while b == 0:
			y = self.random_pos()
			x = self.random_pos()
			if y == 0 and x == 0:
				y = self.random_pos()
				x = self.random_pos()
			if self.raw_map[y][x] == 0:
				self.raw_map[y][x] = 4
				b += 1

	def make_map_texture(self):
		self.map_texture = []
		for i in range(10):
			for e in range(10):
				if self.raw_map[i][e] == 0:
					self.map_texture.append(Tile(self.canvas, e, i))

				elif self.raw_map[i][e] == 1:
					self.map_texture.append(Wall(self.canvas, e, i))

				elif self.raw_map[i][e] == 3:
					self.map_texture.append(Tile(self.canvas, e, i))
					self.map_texture.append(Skeleton(self.map_level, self.canvas, e, i))

				elif self.raw_map[i][e] == 4:
					self.map_texture.append(Tile(self.canvas, e, i))
					self.map_texture.append(Boss(self.map_level, self.canvas, e, i))

		return self.map_texture

	def wall_positions(self):
		return [i.position for i in self.map_texture if type(i) == Wall]

	def tile_positions(self):
		return [i.position for i in self.map_texture if type(i) == Tile]

	def monster_positions(self):
		return [i.position for i in self.map_texture if type(i) == Skeleton or type(i) == Boss]

	def boss_position(self):
		return [i for i in self.map_texture if type(i) == Boss]

	def get_monster(self):
		return [i for i in self.map_texture if i.position == self.hero.position \
					 and type(i) != Tile]

	# def move_monsters(self):
	# 	for monster in self.map_texture:
	# 		if type(monster) == Skeleton or type(monster) == Boss:
	# 			monster.position['x'] += 1
	# 			if monster.position in self.wall_positions():
	# 				monster.position['x'] -= 2
	# 				if monster.position in self.wall_positions():
	# 					monster.position['x'] += 1
	# 					monster.position['y'] += 1
	# 					if monster.position in self.wall_positions():
	# 						monster.position['y'] -= 2
	# 	self.make_map_texture()


	def is_valid_move(self):
		if self.hero.position in self.wall_positions():
			return False
		if not self.hero.position['x'] in range(10):
			return False
		if not self.hero.position['y'] in range(10):
			return False
		return True

	def is_valid_attack(self):
		if self.hero.position in self.monster_positions() + self.boss_position():
			return True
		return False