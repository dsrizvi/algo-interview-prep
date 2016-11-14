# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
class Solution:
	# @return an integer
	def threeSumClosest(self, num, target):
		num.sort()
		diff = float("infinity")

		if len(num) < 3:
			return None

		for i in range(len(num)-2):
			j = i+1
			k = len(num)-1
			while j<k:
				sum = num[i] + num[j] + num[k]
				if abs(sum - target) < diff:
					diff = abs(sum - target)
					answer = sum
				if sum > target:
					k-=1
				else:
					j+=1

			return answer


def main():
	S = Solution()
	# num = [-1,0,1,2,-1,-4]
	num = [-1,2,1,-4]
	print S.threeSumClosest(num, 1)

if __name__ == '__main__':
			main()