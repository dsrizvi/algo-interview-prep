class Solution:
    # @param s, a string
    # @return a string

	def reverseWordsCheating(self, s):
		return ' '.join(reversed(s.split(' ')))

	def reverseWordsActual(self, s):
		length = len(s)
		word = ''
		sentence = ''
		for c in range(length - 1, -1, -1):
			if s[c] != ' ':
				word += s[c]
			else:
				sentence += ' ' + ''.join(reversed(word))
				word = ''

		return sentence

def main():
	print Solution.reverseWordsActual(Solution(),"the sky is blue")

main()