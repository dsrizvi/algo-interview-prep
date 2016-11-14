num_rocks = input()

set_array = []

for n in range(0,num_rocks):
	gem = raw_input()
	char_set = set()

	for char in gem:
		char_set.add(char)

	set_array.append(char_set)

print len(set.intersection(*set_array))

		
