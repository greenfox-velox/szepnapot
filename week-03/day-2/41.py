students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
				]

def students4Candies(lista):
	candidate_count = 0
	for i in lista:
		if i['candies'] > 4 :
			candidate_count += 1
	return candidate_count


print(students4Candies(students))