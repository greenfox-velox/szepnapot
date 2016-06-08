import random

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
			print(self.end())
		elif len(str(guess)) < 4 or len(str(guess)) > 4:
			return "Invalid input: {}".format(guess)
		else:
			self.guess = int(guess)
			return True

	def cow_check(self):
		if self.cows == 4 or guess == self.secret:
			print(self.end())
		return False

	def guess_compare(self, guess_digits, secret_digits):
		self.count += 1
		self.cows = 0
		self.bulls = 0
		for i in range(len(guess_digits)):
			if guess_digits[i] == secret_digits[i]:
				self.cows += 1
			elif guess_digits[i] in secret_digits:
				self.bulls += 1

	def guess_result(self, guess):
		self.guess_valid(guess)
		if not self.cow_check():
			guess_digits = list(str(guess))
			secret_digits = list(str(self.secret))
			self.guess_compare(guess_digits, secret_digits)
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
		# print(cb.count)
		guess = input("Enter guess: >> ")
		print(cb.guess_result(guess))
