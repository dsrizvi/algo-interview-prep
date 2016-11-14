# def twoSumHash(array, value):
# 	numberHash = {}
# 	results = []

# 	for number in array:
# 		if (value - number) in numberHash:
# 			results.append([number, numberHash[value-number]])
# 		numberHash[number] = number

# 	return results


def twoSum(array, value):
	numHash = {}
	results = []

	for number in array:
		if (value - number) in numHash:
			results.append([number, value - number])
		numHash[number] = number

	return results


def main():
	array =	[-1,-4,8,9,-5,12]
	print twoSum(array, 4)
	# print(twoSumSearch(sorted(array), 4))

if __name__ == '__main__':
		main()