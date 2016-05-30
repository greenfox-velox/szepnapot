import unittest
from pocok_work import is_anagramm, letter_count

class DayOneTestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_is_anagramm_basic(self):
		self.assertTrue(is_anagramm("Madam Curie", "Radium came"))

	def test_is_anagramm_without_string(self):
		self.assertFalse(is_anagramm(123, "Yolo"))

	def test_is_anagramm_different_lenght(self):
		self.assertFalse(is_anagramm("Abba", "ab"))

	def test_is_anagramm_empty_input(self):
		self.assertFalse(is_anagramm("", ""))

	def test_is_anagramm_random_anagramms(self):
		self.assertTrue(is_anagramm("Arrigo Boito", "Tobia Gorrio"))
		self.assertFalse(is_anagramm("Ted Morgan", "dEt Yorgen"))

	def test_isanagramm_random_letter_words(self):
		word1 = str(range(1, 6))
		word2 = str(range(1, 6))
		self.assertFalse(is_anagramm(word1, word2))

	def test_letter_count_compare_with_Hello(self):
		hello_count = {'H': 1, 'l': 2, 'o': 1, 'e': 1}
		self.assertEqual(hello_count, letter_count("Hello"))

	def test_letter_count_int_input(self):
		self.assertFalse(letter_count(123))

	def test_letter_count_long_string(self):
		long_string = "abcdefghijklmnopqrst" * 100
		a_count = 100
		self.assertEqual(a_count, letter_count(long_string)['a'])

if __name__ == '__main__':
	unittest.main()