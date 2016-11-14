def moveZero(array):
	end = len(array)-1
	start = 0

	while end >= start:
		print "start:", start
		print "end:", end
		print array
		if array[start] == 0:
			for i in range(start, end):
				array[i], array[i+1] = array[i+1], array[i]
			end  -= 1
		start += 1


	return array

def main():
	array= [0,0,1,3,0,9,8,1]
	print moveZero(array)

if __name__ == '__main__':
	main()