
def allAnagrams(words):
	wordHash = {}
	for word in words:
		sortedWord = ''.join(sorted(word))
		if sortedWord in wordHash:
			wordHash[sortedWord].append(word)
		else:
			wordHash[sortedWord] = [word]

	return wordHash.values()





def main():
	data = ['trees', 'bike', 'cars', 'steer', 'arcs']
	data = ['heir', 'hire', 'erih', 'hoes', 'shoe', 'hose', 'idea', 'aide']

	print allAnagrams(data)

if __name__ == '__main__':
	main()