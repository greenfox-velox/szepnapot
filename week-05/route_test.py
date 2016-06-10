import unittest
import sys
import getopt

from route import Routing

class RoutingTest(unittest.TestCase):

	def setUp(self):
		self.r = Routing()

	def test_without_argument(self):
		self.assertRaises(getopt.GetoptError, self.r.arg_validator, "-b")