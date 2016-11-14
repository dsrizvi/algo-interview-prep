def count(start, end):
	count = 0

	for i in range(start,end+1):
		if i%3 == 0 and i%5 == 0:
			count+=15
		elif i%3 == 0:
			count+=3
		elif i%5 == 0:
			count+=5
		else:
			count+=1


	return count

def main():
	print count(3,117)

if __name__ == '__main__':
	main()