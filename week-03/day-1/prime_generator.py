import math


def isPrime (primeList, candidate):
	upperLimit = math.sqrt(candidate)
	for p in primeList:
		if candidate % p == 0:
			return False
		if p >= upperLimit:
			break
	return True


def primeList(listLength):
	if listLength < 1 :
		return []
	primes = [2]
	candidate = 3
	while listLength > len(primes):
		if isPrime(primes, candidate):
			primes.append(candidate)
		candidate +=2
	print(primes)


prime_len = int(input("How many primes U want?"))

primeList(prime_len)

