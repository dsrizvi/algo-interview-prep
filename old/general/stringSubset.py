def subsets(word, results):
	j = 0
	results = []

	while j <= len(word):
		i = j
		while i <= len(word):
			results.append(word[j:i])
			i += 1
		j += 1

	return results



def main():
	word = "superman"
	results = []
	print subsets(word, results)

if __name__ == '__main__':
	main()