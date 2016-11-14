num_sticks = input()

sticks = [int(i) for i in raw_input().split()]

while num_sticks > 0:
	print num_sticks
	min_stick = min(sticks)
	num_sticks = num_sticks - sticks.count(min_stick)
	sticks = [x for x in sticks if  x != min_stick]


