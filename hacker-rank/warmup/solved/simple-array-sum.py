# https://www.hackerrank.com/challenges/simple-array-sum


import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr_sum = 0

for e in arr:
	arr_sum += e

print e