####################
# OLDER QUESTIONS
####################

# 1. Given a number n, give me a function that returns the nth fibonacci number.
#    Running time, space complexity, iterative vs. recursive.

def fib_iterative(n):
	a, b = 0 , 1
	for __ in range(n):
		a, b = a + b, a
	return a

def fib_recursive(n):
	if n  == 0:
		return n
	if n  == 1:
		return n
	return fib_recursive(n-1) + fib_recursive(n-2)

# 2. Implement integer division without using / or %. Questions about running time. Can you do it faster?

def divide(number, divsor):

	result = 0

	if divsor == 1:
		return number

	while number - divsor >= 0:
		number -= divsor
		result += 1
	return result


# 3. Given an array of numbers and a number k, find if two numbers in the array add up to k. Running time, space complexity, standard questions.

def twoSumHash(array, target):
	numbers = {}
	results = []
	print array
	for i in array:
		if (target - i) in numbers:
			results.append([i,numbers.get(target - i)])
		numbers.update({i: i})
		print numbers
	return results


# 4. Given two sorted arrays and a number k, find the kth largest number in the union of the two arrays. Do it in place and in O(log n)

# 5. Delete a node on a binary search tree.

# 6. Write a program, input a number.

# 7. This program would repeat certain set of mathematical operations (Take digits out of number and square the digits, combine the sum)
#    If at any point the sum is 1, return true, otherwise return false.

def seven(num):

	digits = []
	while num > 0:
		digits += [num % 10]
		num //= 10

	sqaured = map(lambda x: x*x, digits)

	iterator = iter(sqaured)
	s = next(iterator)
	for square in iterator:
		s = square + s
		if s == 1:
			return True

	return False




####################
# NEWER QUESTIONS
####################

# How to tell if there are valid parentheses pairs?
# ex. () --> valid
# )( --> invalid

# Given a passage, text, book, etc., how would you parse it for proper nouns?

def pnouns(text):
	pnouns = filter(lambda x: True if x[0].isupper() else False, text.split(" "))
	return pnouns


# Decide for given integer x and y, if (x^1/3 + y^1/3)^3 is an integer.

# How to insert into sorted list of intervals?

# Show how to rank items in an array using linear space.

 # One of the questions was to find the words in the dictionary that has one edit distance with an input word.

 ####################
 # NEWER FULLTIME SWE
 ####################

 # Given an array where all numbers except one are repeated, find the number that only occurs once.

def nonrepeated(nums):
	countDict = {}

	for num in nums:
		if num in countDict:
			countDict[num] += 1
		else:
			countDict[num] = 1

	for k,v in countDict.items():
		if v == 1:
			return k

	return None

# Create a program that will count the number of common terms between an arithmetic and geometric sequence.

 # Print all the paths from a root to the leaves of a binary tree.

# Given a directory of files and folders. Go through and return all the phone numbers that are contained in the files. (Initial Interview)

# Implement Integer.parseInt()

# You're given a large file that contains sorted log messages. Each log message is a timestamp followed by a log message. Given a range of timestamps, find all the log messages within the timestamp range.

# You are given a function that is running slow, how do you improve it?

# Given a list of strings, find the longest common prefix.

# Implement binary search.


