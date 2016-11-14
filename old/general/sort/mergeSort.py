def mergeSort(array):
	if len(array) < 2:
		return array

	mid = len(array)/2
	left = array[:mid]
	right = array[mid:]

	left = mergeSort(left)
	right = mergeSort(right)

	return merge(left, right)


def merge(left, right):
	merged = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			merged.append(left[i])
			i = i + 1
		else:
			merged.append(right[j])
			j = j + 1
	while i < len(left):
		merged.append(left[i])
		i= i + 1
	while j < len(right):
		merged.append(right[j])
		j = j + 1

	return merged

def main():
	print mergeSort([6,3,5,7,8,11])

if __name__ == '__main__':
	main()
