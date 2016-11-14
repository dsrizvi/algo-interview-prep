# https://leetcode.com/problems/valid-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
	# @return a boolean
	def isValid(self, s):
		stack = []

		for i in range(len(s)):
			if s[i] == '(' or s[i] == '[' or s[i] == '{':
				stack.append(s[i])
			else:
				if len(stack)==0:
					return False
				lastOpenParenthesis = stack.pop()

		if (s[i]==')' and lastOpenParenthesis !='(') or (s[i]==']' and lastOpenParenthesis !='[') or (s[i]=='}' and lastOpenParenthesis !='{'):
			return False

		return len(stack)==0

def main():
	S = Solution()
	s = "()[]{}"
	print S.isValid(s)

if __name__ == '__main__':
	main()