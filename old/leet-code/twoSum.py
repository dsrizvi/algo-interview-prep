# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		numHash= {}
		results = []

		for i in range(len(num)):
			if target - num[i] in numHash:
				return numHash[target-num[i]]+1, i+1
			else:
				numHash[num[i]] = i

		return -1


def main():
	num = [2, 7, 11, 15]
	target = 9
	S = Solution()
	print S.twoSum(num,target)

if __name__ == '__main__':
    		main()