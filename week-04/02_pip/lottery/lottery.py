# Create a method that returns the five most frequent lottery number in a pretty table format
from prettytable import PrettyTable, from_csv
import csv

#Year;Week;Date;Winner;Price won;Weeks without winner;Price total;3 bingos;Price for 3;1 bingos;Price for 1;Number1;Number2;Number3;Number4;Number5

def five_most_frequent():
	numbers_freq = {}
	with open('otos.csv', newline='') as f:
		reader = csv.reader(f)
		for row in reader:
			columns_in_list = (''.join(row).split(';'))
			numbers = columns_in_list[11:]
			for num in numbers:
				numbers_freq[num] = numbers_freq.get(num, 0) + 1
	print(numbers_freq)
	number_csv = PrettyTable(["number", "frequency"])
	for k, v in numbers_freq.items():
		number_csv.add_row([k, v])
	print(number_csv.get_string(sortby="frequency", reversesort=True))

five_most_frequent()