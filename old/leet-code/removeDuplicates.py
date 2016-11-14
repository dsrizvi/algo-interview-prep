class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        S = set(A)
        A = list(S)
        return len(A)

def main():
	print Solution.removeDuplicates(Solution(), [1,1,2])        

main()