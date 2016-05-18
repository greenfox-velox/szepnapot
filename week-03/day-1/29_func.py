def credit_calc(ab=123, credits=100 , is_bonus=False):
	if not is_bonus:
		if credits >= 50:
			ab -= 2
		else:
			ab -= 1
	return ab

print(credit_calc(is_bonus=True))
print(credit_calc(credits=49))