# https://www.hackerrank.com/challenges/diagonal-difference

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

i = 0
p_sum = 0
s_sum = 0

for row in a:
	p_sum += row[i]
	s_sum += row[(n - 1) - i]
	i += 1

print(abs(p_sum - s_sum))

