zoo = ('wolf','tiger','cottonmouth','monkey')
print(zoo.index('cottonmouth'))

for animal in zoo:
	if animal is 'monkey':
		print("I've found a monkey!!")

if 'monkey' in zoo:
	print("I've found a monkey again!!")

# (lizard, fox, mammoth) = zoo 	#does this work?
# print(zoo)

my_zoo = list(zoo)
print(type(zoo), my_zoo)

my_zoo.extend(['python','elephant','lion'])
print(my_zoo)

zoo = tuple(my_zoo)
print(type(zoo))
print(zoo)