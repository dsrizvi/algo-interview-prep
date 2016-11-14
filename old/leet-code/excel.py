# https://leetcode.com/problems/excel-sheet-column-number/
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28


class Solution:
	# @return a string
	def titleToNumber(self, s):
		answer = 0
		j = len(s)-1
		for i in range(0,j+1):
			answer+= (ord(s[i])-64)*(26**(j-i))

		return answer

def main():
	title = 'B'
	S = Solution()
	print Solution.titleToNumber(S,title)

if __name__ == '__main__':
			main()


