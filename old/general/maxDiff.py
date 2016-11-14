import math

# def maxDiff(numbers):

# 	maxNum = numbers[0]
# 	minNum = numbers[1]
# 	for number in numbers:
# 		minNum = min(number, minNum)
# 		maxNum = max(number, maxNum)

# 	return maxNum - minNum


def maxDiff(numbers):

	maxDiff = 0

	for number in numbers:
		maxDiff= max(maxDiff)









def main():
	numbers = [1,7,3,9,4,11,13]
	numbers = [2,3,4,1,99,1,1111,93]
	print maxDiff(numbers)

if __name__ == '__main__':
	main()