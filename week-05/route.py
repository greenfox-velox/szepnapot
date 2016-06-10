import sys
import getopt

class Parser():
	"""parse cml arguments,give proper call to controller"""

	def __init__(self, argv):
		self.argv = argv
		self.options_short = "larc"
		self.opt = None
		self.passed_arg = None
		if self.arg_validator(self.argv) != getopt.GetoptError:
			self.arg_parser()

	def arg_validator(self, argv):
		try:
			self.opts, self.args = getopt.getopt(argv, self.options_short)
			return self.opts, self.args
		except getopt.GetoptError or len(argv) < 1:
			return getopt.GetoptError

	def arg_parser(self):
		for opt, arg in self.opts:
			if opt in ("-a", "-r", "-c"):
					try:
						self.passed_arg = arg[0]
						self.opt = opt
						return self.opt, self.passed_arg
					except IndexError:
						return "Unable to complete request: No task is provided"
			else:
				return Exception

p = Parser(sys.argv[1:])
print(p.passed_arg)