# https://www.hackerrank.com/challenges/angry-professor
import sys

def class_check(arrival_times, min_students):
	class_cancelled = "YES" if len([x for x in arrival_times if x <= 0]) < min_students else "NO"
	return class_cancelled



def main():
	import sys

	t = int(input().strip())
	for a0 in range(t):
	    n,k = input().strip().split(' ')
	    n,k = [int(n),int(k)]
	    a = [int(a_temp) for a_temp in input().strip().split(' ')]
        print(class_check(a, k))

if __name__ == '__main__':
	main()
