
def longestConsecutive(num):

	if len(num) < 1:
		return None

	maxLen = 0

	numHash = {key: key for key in num}

	for i in numHash.keys():
		localLen = 1

		j = 1
		while numHash.get(numHash[i]+ j):
			localLen+=1
			j+=1
			# print localLen

		maxLen = max(localLen, maxLen)


	return maxLen

def main():
	a = [100, 4, 200, 1, 3, 2]
	print longestConsecutive(a)

if __name__ == '__main__':
	main()