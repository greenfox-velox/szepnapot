def fibonaccis(n):
	i = 0
	previous = [0]
	while len(previous) < n:
		if len(previous) < 3:
			previous.append(1)
		i =  previous[-1] + previous[-2]
		previous.append(i)
	return previous

print(fibonaccis(50))