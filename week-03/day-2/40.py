students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
def candidates_u10(lista):
	candidate_count = 0
	for i in lista:
		if i['age'] < 10 :
			candidate_count += i['candies']
	return candidate_count


print(candidates_u10(students))
