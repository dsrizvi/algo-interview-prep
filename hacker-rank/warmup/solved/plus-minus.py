# https://www.hackerrank.com/challenges/plus-minus

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

p_num,n_num,z_num = 0,0,0

for e in arr:
	if e > 0:
		p_num += 1
	elif e < 0:
		n_num += 1
	else:
		z_num += 1

print(p_num/n)
print(n_num/n)
print(z_num/n)