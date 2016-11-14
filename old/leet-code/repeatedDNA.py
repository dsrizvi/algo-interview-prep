# https://leetcode.com/problems/repeated-dna-sequences/
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].


class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
    	if len(s) < 10:
    		return []

    	seen = set()
    	results = set()
    	i = len(s) - 9
    	j = 0

    	while j < i:
    		if s[j:j+10] in seen:
    			results.add(s[j:j+10])
    		else:
    			seen.add(str(s[j:j+10]))
    		j+=1

    	return list(results)

# ["AAAAAAAAAA","AAAAAAAAAA"]
def main():
	s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
	s2 = 'AAAAAAAAAAAA'
	S = Solution()
	print Solution.findRepeatedDnaSequences(S,s2)

if __name__ == '__main__':
    		main()