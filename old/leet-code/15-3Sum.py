
class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		num = sorted(num)
		results = []
		if len(num) < 3:
			return results

		for i in range(len(num)-2):
			j = i+1
			k = len(num)-1

			while k>j:
				sum = num[i] + num[j] + num[k]
				if sum == 0:
					# if [num[i],num[j],num[k]] not in results:
					results.append([num[i],num[j],num[k]])
					break
				if sum > 0:
					k-=1
				if sum < 0:
					j+=1

		return results

def main():
	S = Solution()
	# num = [-1,0,1,2,-1,-4]
	num = [-2,0,1,1,2]
	print S.threeSum(num)

if __name__ == '__main__':
			main()