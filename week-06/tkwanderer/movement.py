from screen import Screen


class Move(object):

	def __init__(self, canvas):
		self.screen = Screen(canvas)
		self.hero_cords = self.screen.coords.hero_position()[0]['x'], self.screen.coords.hero_position()[0]['y']

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
		self.out_of_map()
		self.screen.draw_map()

	def move_down(self):
		self.screen.coords.hero_position()[0]['y'] += 1
		self.out_of_map()
		self.screen.draw_map()

	def move_right(self):
		self.screen.coords.hero_position()[0]['x'] += 1
		self.out_of_map()
		self.screen.draw_map()

	def move_left(self):
		self.screen.coords.hero_position()[0]['x'] -= 1
		self.out_of_map()
		self.screen.draw_map()

	def is_wall(self):
		if self.hero_cords in self.screen.coords.wall_positions():
			return True

	def out_of_map(self):
		if not self.hero_cords[0] in list(range(9)):
			print(self.hero_cords[0])
			print("Out!")
		elif not self.hero_cords[1] in list(range(9)):
			print("Out!")