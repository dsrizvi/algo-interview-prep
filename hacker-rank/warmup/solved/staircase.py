# https://www.hackerrank.com/challenges/staircase

import sys

def build_staircase(total_steps):
	curr_step = 1

	while curr_step <= total_steps:
		spaces = ' ' * (total_steps - curr_step)
		hashtags = '#' * curr_step
		print(spaces + hashtags)
		curr_step += 1

	return

def main():
	total_steps = int(input().strip())
	build_staircase(total_steps)


if __name__ == '__main__':
	main()