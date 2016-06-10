from collections import Counter

def fahrenheit(t):
	return (9/5.0 * t + 32)

def celsius(t):
	return (5/9.0 * (t - 32))

temps = [36.5, 40, 50, 25, 39, 37.5]

# print(list(map(fahrenheit, temps)))


# print(list(map(lambda t: 9/5.0 * t + 32, temps)))





# fh = list(map(lambda x: 9/5.0 * x + 32, temps))
#
# print(list(map(lambda x: 5/9.0 * (x - 32), fh)))


################################################################



a = [1, 2, 3, 4]
b = [-1, -2, -3, -4]
c = [2, 4, 6, 8]



# print(list(map(lambda x, y, z: x + y + z, a, b, c)))



################################################################
################################################################
################################################################
##########              FILTER        ##########################
################################################################
################################################################
################################################################



lista1 = ['Budapest', 'San Francisco', 'London', 'New York', 'Becs', 'Parizs']

lista2 = list(range(1, 101))

fibos = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

random_coords = [{'type': 'hero', 'y': 0, 'x': 0}, {'type': 'tile', 'y': 0, 'x': 1},
								 {'type': 'tile', 'y': 0, 'x': 2}, {'type': 'wall', 'y': 0, 'x': 3}]



# print(list(filter(lambda x: x % 2, lista2)))


# def is_two_word(word):
# 	try:
# 		word.split()[1]
# 		return True
# 	except IndexError:
# 		return False
#
# print(list(filter(is_two_word, lista1)))

# print(list(filter(lambda x: x.split()[1], lista1)))



# print(list(filter(lambda x: not x % 2, fibos)))





# print(list(filter(lambda x: x['type'] == 'wall', random_coords)))




################################################################
################################################################
################################################################
##########          COMPREHENSIONS        ######################
################################################################
################################################################
################################################################


evens_till_100 = list(range(0, 101, 2))

evens_comp = [i for i in range(101) if i % 2 == 0]

# evens = []
# for i in range(101):
# 	if i % 2 == 0:
# 		evens += i
#
# print(evens_comp)



# evens_comp = [x * 2 for x in range(51)]




# evens_conditional = [x for x in range(101) if x % 2 == 0]





# evens_if_else = ['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in range(1, 101)]
#
# print(evens_if_else)




### DICTIONARY TRICK

long_string = """Lorem ipsum dolor sit amet, quo id ridens senserit mnesarchum, adhuc solum nonumes an sea. Augue ponderum ut eam, te causae deserunt mnesarchum pro. Natum detracto mel ad, quando detracto ne duo, ad nominavi definitiones eum. Vide mnesarchum interpretaris eu vel.
Sed in putent causae. Vidit populo explicari est in, luptatum expetenda sententiae et has, cu vim odio esse. Stet postea eos an. Ludus iriure nec in, labores sapientem et nam. Doctus definitionem pri ex.
Duo ea vidisse molestiae. Nec id hinc praesent. At his nibh dolor minimum, porro ullamcorper nam id. Movet omnesque no ius. Vim facilisi liberavisse ut, an ipsum viris mnesarchum vix. Ut quo munere concludaturque, cum iusto mentitum an. Nisl saepe postulant mel et.
No sed porro sadipscing, labore eligendi vis ea, prompta gloriatur ne mel. Sea laudem libris nostrum eu. Cu augue gloriatur his, feugiat debitis epicuri ea eam, mucius equidem salutandi est ne. Eirmod sententiae at pri, cu usu suscipit convenire maluisset, nominati similique ex mea. Consul quodsi platonem mea at. Ut vis alii instructior.
Wisi melius delectus te sit, ea soleat denique has. In rebum clita quo, ad modo lucilius gubergren sea. Ei invenire contentiones vis, ea mazim aeterno vel. Id nec solum constituto deseruisse, ius dolorem intellegebat id, mei inani dicunt ea. Tamquam civibus oportere vim et, choro partem id est. Alienum phaedrum sea ea, nec alii salutandi an."""


# chars = {}
# for c in long_string:
# 	chars[c] = chars.get(c, 0) + 1
# print(chars)






# chars = {}
# for c in long_string:
# 	chars[c] = chars.get(c, 0) + 1
# print(chars)

# print(Counter(long_string))



