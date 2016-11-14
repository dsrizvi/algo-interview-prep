# https://leetcode.com/problems/excel-sheet-column-title/
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB


class Solution:
    # @return a string
    def convertToTitle(self, num):
        answer = ""

        while num > 0:
            if num%26 == 0:
                answer+= "Z"
                num=num/26-1
            else:
                answer += chr(num%26 + 64)
                num= num/26


        return answer[::-1]



def main():
    title = 26
    S = Solution()
    print Solution.convertToTitle(S,title)

if __name__ == '__main__':
            main()


