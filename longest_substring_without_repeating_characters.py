# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3.
#
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        resultCount = 0
        temp = ""
        for c in s:
            if c in temp:
                if resultCount < len(temp):
                    resultCount = len(temp)
                temp = temp[temp.find(c) + 1:] + c
            else:
                temp += c
        return len(temp) if len(temp) > resultCount else resultCount

print Solution().lengthOfLongestSubstring("f")
