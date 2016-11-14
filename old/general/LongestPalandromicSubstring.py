def LPS(s):
	n = len(s)
	table = [n][n]

	maxLen = 1
	for i in range(n):
		table[i][i] = True

	start = 0
	for i in range(n):

		if s[i] == s[i+1]:
			table[i][i+1] = True
			start = i
			maxLen = 2

	for i in range(3,n):
		for j in range





def main():
	print LPS("forgeeksskeegfor")

if __name__ == '__main__':
	main()