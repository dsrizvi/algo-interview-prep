
def twoSum(array, sum):
	numbers = {}
	results = []

	for i in array:
		numbers.update({i: i})

	for i in array:
		if (sum - i) in numbers:
			results.append([i,numbers.get(sum - i)])
			del numbers[i]

	return results


def threeSum(array, sum):
	array.sort()
	results = []


	for i in array:
		if i < 0:
			pass
		else:
			temp = twoSum(array, sum-i)
			if temp:
				temp.append(i)
				results.append(temp)

	return results




def main():
	array =	[-1,-4,8,0,9,-5,12]
	# print(twoSum(array, 4))
	print(threeSum(array,4))

if __name__ == '__main__':
	main()