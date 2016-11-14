class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
    	num = sorted(num)

    	for i in range(len(num)-1):
    		j = i+1
    		k = len(num)

    		while k>=j:
    			sum = num[i] + num[j] + num[k]
    			if sum == 0
    				return num[i],num[j],num[k]

    			if sum > 0:
    				k-=1
    			if sum < 0:
    				j-=0


def main():
    title = 26
    S = [-1, 0, 1, 2, -1, -4]
    print S.threeSum(num)

if __name__ == '__main__':
            main()