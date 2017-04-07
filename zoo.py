zoo = ('wolf','tiger','cottonmouth')
print(zoo.index('cottonmouth'))

for animal in zoo:
	if animal is 'monkey':
		print("I've found a monkey!!")

(lizard, fox, mammoth) = zoo
print(lizard)

zoo = list(zoo)
print(type(zoo))

zoo.extend(['python','elephant','lion'])
print(zoo)

zoo = tuple(zoo)
print(type(zoo))
print(zoo)