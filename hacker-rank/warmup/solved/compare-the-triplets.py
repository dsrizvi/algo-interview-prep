# https://www.hackerrank.com/challenges/compare-the-triplets

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a_ratings = [a0, a1, a2]
b_ratings = [b0, b1, b2]

a_score = 0
b_score = 0

for a,b in zip(a_ratings, b_ratings):
	if a > b:
		a_score += 1
	elif b > a:
		b_score +=1

print(a_score,b_score)