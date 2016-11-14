
for _ in range (input()):
	n = int(raw_input())
	a = 0
	if n%2 == 0:
		a = pow(n/2,2)
	else:
		b = int(round(n/2) )
		a = b*(b+1) 	
	print a