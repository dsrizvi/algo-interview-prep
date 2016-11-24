# https://www.hackerrank.com/challenges/repeated-string

import sys


s = input().strip()
n = int(input().strip())

def count_a(s,n):
    len_s = len(s)
    full_repeats = n//len_s
    remainder_chars = n%len_s

    return (s.count('a')*full_repeats + s[0:remainder_chars].count('a'))

def main():
    s = input().strip()
    n = int(input().strip())
    print(count_a(s,n))

if __name__ == '__main__':
	main()