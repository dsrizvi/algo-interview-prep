
def replaceWord(string, toReplace, replacement):
	words = string.split()

	index = words.index(toReplace)
	words[index] = replacement

	string = ' '.join(words)

	return string








def main():
	print replaceWord("the dog is the best", "best", "greatest")

if __name__ == '__main__':
	main()