def findPivot(array, left, right):

	if left > right:
		return -1
	if left == right:
		return left

	mid = (left+right)/2

	if array[mid-1] > array[mid]:
		return array[mid]
	if array[mid+1] < array[mid]:
		return array[mid+1]

	if array[mid] > array[right]:
		return findPivot(array, mid+1, right)
	else:
		return findPivot(array, left, mid-1)


def main():
	array = [4,5,6,7,1,2,3]
	array2 = [7,1,2,3,4,5,6]
	array3 = [7,8,9,1,2,3,4,5,6]
	print findPivot(array3, 0, len(array3)-1)

if __name__ == '__main__':
	main()