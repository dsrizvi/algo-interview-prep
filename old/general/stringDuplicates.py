
def duplicates(string):

	words = string.split()

	seen = set()
	duplicates = []

	for word in words:
		if word in seen:
			duplicates += [word]
		seen |= {word}

	return duplicates





def main():
	print duplicates("the dog is the best best")

if __name__ == '__main__':
	main()
