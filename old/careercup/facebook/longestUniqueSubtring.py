#http://www.careercup.com/page?pid=facebook-interview-questions

def longestRepeated(string):

	seen = set()
	substrings = []
	answer = ''
	for i in range(len(string)):
		substring = string[i]
		seen = set(string[i])
		for j in range(i+1, len(string)):
			if string[j] in seen:
				if len(substring) > len(answer):
					answer = substring
				break
			else:
				seen.update(string[j])
				substring +=string[j]

	return answer




def main():
	print(longestRepeated("abbabcdaa"))


if __name__ == '__main__':
	main()