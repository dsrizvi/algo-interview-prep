def recusriveBinarySearch(array, value, left, right):

	middle = left + (right- left)/2

	if array[middle] == value:
		return middle

	if left == right:
		return -1

	if array[middle] > value:
		return recusriveBinarySearch(array, value, left, middle)
	else:
		return recusriveBinarySearch(array, value, middle + 1, right)

def iterativeBinarySearch(array, value, left, right):

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
	array = [0,1,2,4,5,6,7]
	array2 = [0,12,23,45,56,78]
	print recusriveBinarySearch(array, 5, 0, 6)
	print iterativeBinarySearch(array2, 78, 0, 6)

if __name__ == '__main__':
	main()