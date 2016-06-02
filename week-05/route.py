import sys, getopt

class Routing():
	"""parse cml arguments
	give proper call to controller"""

	def __init__(self, argv):
		self.options_short = "larc:d"
		self.options_long = ["list", "add", "remove", "complete"]
		self.argv = argv
		self.validator()

	def validator(self):
		try:
			self.opts, self.args = getopt.getopt(self.argv, self.options_short, self.options_long)
		except getopt.GetoptError or len(self.argv) < 1:
			return getopt.GetoptError
		return self.opts, self.args

	def route(self):
		for opt, arg in self.opts:
			if opt in ("-l", "--list"):
				return "-l"
			elif opt in ("-a", "--add"):
				try:
					return "-a", arg[0]
				except IndexError:
					print("Unable to add: No task is provided")
			elif opt in ("-r", "--remove"):
				try:
					return "-r", int(arg[0])
				except IndexError:
					print("Unable to add: No task is provided")
				except ValueError:
					print("Unable to remove: Index is out of bound")
			elif opt in ("-c", "--complete"):
				pass