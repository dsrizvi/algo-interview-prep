def findMin(array):
	return findMinHelper(array, 0, len(array)-1)

def findMinHelper(array, left, right):

	if left > right:
		return array[0]

	if left == right:
		return array[left]

	mid = (right+left)/2

	if array[mid] > array[mid+1]:
		return array[mid+1]

	if array[mid-1] > array[mid]:
		return array[mid]

	if array[mid] < array[right]:
		return findMinHelper(array, left, mid-1)
	else:
		return findMinHelper(array, mid+1, right)


def main():
	array = [4,5,6,7,1,2,3]
	array2 = [7,1,2,3,4,5,6]
	array3 = [6,8,9,10,11,3,4]
	print findMin(array3)

if __name__ == '__main__':
	main()