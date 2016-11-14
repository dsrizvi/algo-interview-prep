# https://leetcode.com/problems/word-break-ii/
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a list of strings
	def wordBreak(self, s, dict):
		solutions = []
		for word in dict:
			temp = ''
			if word in s:
				temp+=word




def main():
	S = Solution()
	s = "catsanddog",
	dict = ["cat", "cats", "and", "sand", "dog"].
	print S.wordBreak(s,dict)