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
		if left[i] < right[j]:
			merged.append(left[i])
			i = i + 1
		elif left[i] > right[j]:
			merged.append(right[j])
			j = j + 1
		else:
			j = j+1
	while i < len(left):
		merged.append(left[i])
		i= i + 1
	while j < len(right):
		merged.append(right[j])
		j = j + 1

	return merged

def main():
	print mergeSort([6,6,3,3,3,3,5,6,6,6,6,5,5,5,5,7,8,11])
	print mergeSort([4,5,3,2])

if __name__ == '__main__':
	main()
