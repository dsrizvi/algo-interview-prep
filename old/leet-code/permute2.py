class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        n=len(num)
        if n<=1:
            return [num]
        rst=[]
        num.sort()
        cur=0
        pre=None
        for cur in range(n):
            if num[cur]==pre:
                continue
            pre=num[cur]
            for i in self.permuteUnique(num[:cur]+num[cur+1:]):
                rst.append(i+[num[cur]])
        return rst
