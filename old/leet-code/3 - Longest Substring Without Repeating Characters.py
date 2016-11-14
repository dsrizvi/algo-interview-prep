# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        length = len(s) - 1
        max_sub = ''

        i = 0
        while i <= length:
            j = i
            sub = ''
            seen = set()
            while j <= length:
                if s[j] not in seen:
                    sub += s[j]
                    seen.add(s[j])
                else:
                    if len(sub) > len(max_sub):
                        max_sub = sub
                        break
                j += 1
            i += 1

        return max_sub

def main():
    s = "abcabcbb"
    s2 = ""
    s3 = 'bbbbb'
    S = Solution()
    print S.lengthOfLongestSubstring(s3)

if __name__ == '__main__':
            main()