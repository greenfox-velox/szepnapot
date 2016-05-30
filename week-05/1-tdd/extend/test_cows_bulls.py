import unittest
import cows_and_bulls
import random


class TestCowsAndBulls(unittest.TestCase):

	def setUp(self):
		"""available methods of CowsAndBulls class:
		help, secret_number, guess_valid, guess_result,
		 printer, end"""
		self.cab = cows_and_bulls.CowsAndBulls()

	def test_cowsAndBulls_exit(self):
		self.cab.guess_valid('end')
		self.assertEqual(self.cab.state, "finished")

	def test_cowsAndBulls_is_exist(self):
		"""unique methods, will fail for other classes"""
		self.assertTrue(self.cab.help)
		self.assertTrue(self.cab.secret_number)
		self.assertTrue(self.cab.guess_valid)
		self.assertTrue(self.cab.guess_result)
		self.assertTrue(self.cab.printer)
		self.assertTrue(self.cab.end)

	def test_cowsAndBulls_secret_generated(self):
		self.assertTrue(self.cab.secret)

	def test_cowsAndBulls_secret_is_correct(self):
		available_numbers = list(range(1000, 9999))
		self.assertIn(self.cab.secret, available_numbers)

	def test_cowsAndBulls_validator_works(self):
		self.assertFalse(self.cab.guess_valid(123))
		self.assertFalse(self.cab.guess_valid(123456))
		self.assertFalse(self.cab.guess_valid("hy validator"))
		self.assertFalse(self.cab.guess_valid(""))
		self.assertFalse(self.cab.guess_valid([]))
		self.assertFalse(self.cab.guess_valid(-1234))
		self.assertFalse(self.cab.guess_valid(-1-2-3-4))

	def test_cowsAndBulls_playing(self):
		self.assertEqual(self.cab.state, 'playing')

	def test_cowsAndBulls_count(self):
		guess = "123"
		guess += str(self.cab.secret)[2]
		self.cab.guess_result(int(guess))
		self.assertEqual(self.cab.count, 1)
		self.assertGreaterEqual(self.cab.bulls, 1)

	def test_cowsAndBulls_end_if_cows_reached(self):
		guess = self.cab.secret
		self.cab.guess_result(guess)
		self.assertEqual(self.cab.cows, 4)
		self.assertEqual(self.cab.state, 'finished')

if __name__ == '__main__':
	unittest.main()
