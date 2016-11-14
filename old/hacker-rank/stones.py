N = int(raw_input())
answer_array = []

for case in range (0,N):
	num_steps = int(raw_input()) - 1 
	# print num_steps
	x = int(raw_input())
	y = int(raw_input())	
	
	a = min(x,y)
	b = max(x,y)
	
	final_step = 0
	print_string = ''
	case_array = []
	for x in range (0, num_steps):
		final_step = a*(num_steps - x) + b*(x)
	
	case_array.append(num_steps*b)	
	answer_array.append(case_array)

for case in answer_array:
	print '%s' % ' '.join(map(str, case))
		