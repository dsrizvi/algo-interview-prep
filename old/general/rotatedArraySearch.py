def findElement(array, left, right, value):

	middle = (right+left)/2

	if left > right:
		return -1

	if left == right:
		return right


	if array[middle] == value:
		return middle

	#left is sorted
	if array[middle] > array[left]:
		#value is in left
		if array[left] <= value <= array[middle]:
			return findElement(array, left, middle-1, value)
		#value is in right
		else:
			return findElement(array, middle+1, right, value)
	#right is sorted
	else:
		#value is in right
		if array[middle] <= value <= array[right]:
			return findElement(array, middle+1, right, value)
		else:
		#value is in left
			return findElement(array, left, middle-1, value)

def main():
	array = [4,5,6,7,1,2,3]
	array2 = [7,1,2,3,4,5,6]
	print findElement(array2, 0, 6, 1)

if __name__ == '__main__':
	main()