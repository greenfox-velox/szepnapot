import unittest
import extend
import random
import operator
import statistics

class TestExtend(unittest.TestCase):
	def setUp(self):
		pass

	def test_add_2_and_3_is_5(self):
		self.assertEqual(extend.add(2, 3), 5)

	def test_add_string(self):
		self.assertFalse(extend.add("harom", 2))

	def test_add_random_numbers(self):
		a = random.randint(1, 10000)
		b = random.randint(1, 10000)
		self.assertEqual(operator.add(a, b), extend.add(a, b))

	def test_add_4_and_1_is_5(self):
		self.assertEqual(extend.add(4, 1), 5)

	def test_add_negative_number(self):
		self.assertEqual(extend.add(-5, -10), -15)

	def test_max_of_three_first(self):
		self.assertEqual(extend.max_of_three(5, 4, 3), 5)

	def test_max_of_three_third(self):
		self.assertEqual(extend.max_of_three(3, 4, 5), 5)

	def test_max_of_three_basic(self):
		a = 10
		b = 5
		c = 12
		self.assertEqual(extend.max_of_three(a, b, c), c)

	def test_max_of_three_string_input(self):
		self.assertFalse(extend.max_of_three(10, 5, "hy"))

	def test_max_of_three_negative_input(self):
		a = random.randint(1, 100)
		b = -30
		c = -40
		self.assertEqual(extend.max_of_three(a, b, c), a)

	def test_max_of_three_empty_inputs(self):
		self.assertFalse(extend.max_of_three('', '', ''))

	def test_max_of_three_all_zeroes(self):
		self.assertEqual(extend.max_of_three(0, 0, 0), 0)

	def test_median_four(self):
		self.assertEqual(extend.median([7,5,3,5]), 5)

	def test_median_five(self):
		self.assertEqual(extend.median([1,2,3,4,5]), 3)

	def test_median_with_built_in(self):
		median_list = [random.randint(1, 500) for i in range(1, 100)]
		self.assertEqual(statistics.median(median_list), extend.median(median_list))

	def test_median_odd_lenght(self):
		median_list = [1, 3, 5, 8, 9]
		self.assertEqual(extend.median(median_list), 5)

	def test_median_even_lenght(self):
		median_list = [1, 3, 8, 9]
		self.assertEqual(extend.median(median_list), 5.5)

	def test_median_empty_list(self):
		self.assertFalse(extend.median([]))

	def test_median_just_negative_unsorted_odd(self):
		median_list = [-5, -2, -1, -55, -9, -4, -3]
		self.assertEqual(extend.median(median_list), -4)

	def test_median_just_negative_unsorted_even(self):
		median_list = [-5, -1, -55, -9, -4, -3]
		self.assertEqual(extend.median(median_list), -4.5)

	def test_median_all_same_number(self):
		median_list = [2, 2, 2, 2, 2, 2]
		self.assertEqual(extend.median(median_list), 2)

	def test_is_vovel_a(self):
		self.assertTrue(extend.is_vovel('a'))

	def test_is_vovel_u(self):
		self.assertTrue(extend.is_vovel('u'))

	def test_translate_bemutatkozik(self):
		self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

	def test_translate_kolbice(self):
		self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

	def test_translate_novowel(self):
		self.assertEqual(extend.translate('ptgrx'), 'ptgrx')

	def test_translate_emptystring(self):
		self.assertEqual(extend.translate(''), '')

	def test_translate_integer(self):
		self.assertFalse(extend.translate(123456))

	def test_translate_digit_inside(self):
		self.assertFalse(extend.translate("Heyy12Yol3"))

	def test_translate_latin_chars(self):
		self.assertEqual(extend.translate("ő és bátyja"), "ővő évés bávátyjava")

	def test_translate_sentence(self):
		self.assertEqual(extend.translate("Hello, there!"), "Hevellovo, thevereve!")

if __name__ == '__main__':
	unittest.main()
