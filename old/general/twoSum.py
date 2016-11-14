
def twoSumHash(array, target):
	numbers = {}
	results = []

	for i in array:
		if (target - i) in numbers:
			results.append([i,numbers.get(target - i)])
		numbers.update({i: i})
	return results


def twoSumSearch(array, target):
	results = []
	for num in array:
		t = binarySearch(array, target - num)
		if t != -1:
			results.append([target-num, num])
			array.remove(num)

	return results


def binarySearch(array, value):
	right = len(array)
	left = 0
	while left < right:
		middle = left + (right- left)/2
		if array[middle] == value:
			return middle
		if value > array[middle]:
			left = middle + 1
		else:
			right = middle

	return -1


def main():
	array =	[-1,-4,8,9,-5,12]
	print(twoSumHash(array, 4))
	print(twoSumSearch(sorted(array), 4))

if __name__ == '__main__':
	main()