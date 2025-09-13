class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        dict_s = dict()
        checkpoint = 0
        for i in range(len(s)):
            if s[i] in dict_s and dict_s[s[i]] >= checkpoint:
                checkpoint = dict_s[s[i]] + 1
            res = max(res, i - checkpoint + 1)
            dict_s[s[i]] = i

        return res