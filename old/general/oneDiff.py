# Given a string and array of strings, find whether the array contains a string with one character difference from the given string. Array may contain string of different lengths.

# Ex: Given string


# banana
# and array is


# [bana, apple, banaba, bonanza, banamf]
# and the output should be true as banana and banaba are one character difference.



def oneDiff(word, dictionary):
	letters = {}

	for c in word:
		if c in letters:
			letters[c] += 1
		else:
			letters[c] = 1

	dict_letters = []
	for w in dictionary:
		w_letters = {}
		for c in w:
			if c in w_letters:
				w_letters[c] += 1
			else:
				w_letters[c] = 1

		dict_letters.append((w, w_letters))
	# print dict_letters

	results = []
	for w in dict_letters:
		diff = 0
		for k in letters:
			if k in w[1]:
				diff = letters[k] - w[1][k]
		if abs(diff) == 1:
			results.append(w[0])

	return results

def main():
	word = 'banana'
	dictionary = ['bana', 'apple', 'banaba', 'bonanza', 'banamf']
	print oneDiff(word, dictionary)


if __name__ == '__main__':
	main()