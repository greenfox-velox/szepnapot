import random
import sys

class CowsAndBulls:

	def __init__(self):
		self.secret = self.secret_number()
		self.state = 'playing'
		self.count = 0
		self.cows = 0
		self.bulls = 0

	def help(self):
		return "To exit enter 'end'\nGood luck!"

	def secret_number(self):
		self.secret = random.randint(1000, 9999)
		return self.secret

	def guess_valid(self, guess):
		if type(guess) == str and guess.lower() == 'end':
			self.end()
		elif len(str(guess)) < 4 or len(str(guess)) > 4:
			return False
		else:
			self.guess = int(guess)
			return True

	def guess_result(self, guess):
		if not self.guess_valid(guess):
			return "Invalid input: {}".format(guess)
		if self.cows == 4:
			self.end()
		self.count += 1
		guess_digits = list(str(guess))
		secret_digits = list(str(self.secret))
		for i in range(len(guess_digits)):
			if guess_digits[i] == secret_digits[i]:
				self.cows += 1
			elif guess_digits[i] in secret_digits:
				self.bulls += 1
		return "{} cows, {} bulls.".format(self.cows, self.bulls)

	def printer(self):
		return "It took you {} guesses. The random number was: {}".format(self.count, self.secret)

	def end(self):
		self.state = 'finished'
		self.printer()

if __name__ == '__main__':
	cb = CowsAndBulls()
	print(cb.help())

	while cb.state == 'playing':
		guess = input("Enter guess: >> ")
		print(cb.guess_result(guess))
