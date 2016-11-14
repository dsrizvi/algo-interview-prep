def sumPair(array, value):
	hashmap = {}
	pairs = []
	for element in array:
		hashmap.update({element:element})
	for element in array:
		if (value - element) in hashmap:
			pair = []
			pair.append(element)
			pair.append(value - element)
			pairs.append(pair)

	return pairs


def main():
	print sumPair([1,7,2,3,0], 3)

if __name__ == '__main__':
	main()