# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.



# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.


class Solution:
	# @return a list of strings, [s1, s2]
	def letterCombinations(self, digits):
		results = []
		mappings = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
		if not digits:
			return []
		results = list(mappings[digits[0]])

		for i in digits[1:]:
			# results = [a+b for a in results for b in mappings[i]]
			z = []
			for a in results:
				for b in mappings[i]:
					 z.append(a+b)
			results = z

		return results



def main():
	S = Solution()
	# num = [-1,0,1,2,-1,-4]
	digit = '234'
	print S.letterCombinations(digit)

if __name__ == '__main__':
	main()