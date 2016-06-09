from screen import Screen

class Move(object):

	def __init__(self, canvas):
		self.screen = Screen(canvas)

	def get_hero_pos(self):
		self.hero_cords = self.screen.coords.hero_position()[0]['x'], self.screen.coords.hero_position()[0]['y']
		return self.hero_cords

	def route(self, key):
		direction = key.keysym
		if direction == 'Up':
			self.move_up()
		elif direction == 'Down':
			self.move_down()
		elif direction == 'Right':
			self.move_right()
		elif direction == 'Left':
			self.move_left()

	def move_up(self):
		self.screen.coords.hero_position()[0]['y'] -= 1
		if self.out_of_map():
			self.move_down()
		if self.is_wall():
			self.move_down()
		self.screen.draw_map()

	def move_down(self):
		self.screen.coords.hero_position()[0]['y'] += 1
		if self.out_of_map():
			self.move_up()
		if self.is_wall():
			self.move_up()
		self.screen.draw_map()

	def move_right(self):
		self.screen.coords.hero_position()[0]['x'] += 1
		if self.out_of_map():
			self.move_left()
		if self.is_wall():
			self.move_left()
		self.screen.draw_map()

	def move_left(self):
		self.screen.coords.hero_position()[0]['x'] -= 1
		if self.out_of_map():
			self.move_right()
		if self.is_wall():
			self.move_right()
		self.screen.draw_map()

	def is_wall(self):
		self.get_hero_pos()
		if self.hero_cords in self.screen.coords.wall_positions():
			return True

	def out_of_map(self):
		self.get_hero_pos()
		if not self.hero_cords[0] in list(range(10)):
			return True
		elif not self.hero_cords[1] in list(range(10)):
			return True