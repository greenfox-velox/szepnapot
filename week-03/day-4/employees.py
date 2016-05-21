employees = [ {'first_name': "Dipper", 'last_name': "Pines", 'role': "Boss"}, {'first_name': "Jpper", 'last_name': "Anes", 'role': "Truck driver"}]

def find_employees_role(name):
	first, last = name.split()[0], name.split()[1]
	for data in employees:
		if data['first_name'] == first:
			return data['role']
		else:
			return "Does not work here!"

print(find_employees_role('Dipper Pines'))


