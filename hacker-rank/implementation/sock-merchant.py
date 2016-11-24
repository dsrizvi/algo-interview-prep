# https://www.hackerrank.com/challenges/sock-merchant

import sys

def count_pairs(socks):
	sock_dict = {}

	for s in socks:
		if s in sock_dict:
			sock_dict[s] = sock_dict[s] + 1
		else:
			sock_dict[s] = 1

	total_pairs = 0
	for c in sock_dict.values():
		total_pairs += (c - (c%2))/2

	return int(total_pairs)

def main():
	n = int(input().strip())
	c = [int(c_temp) for c_temp in input().strip().split(' ')]

	print(count_pairs(c))


if __name__ == '__main__':
	main()
