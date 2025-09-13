class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        n = len(s)
        res = s[0]
        max_len = 1
        for i in range(n):
            for j in range(i + 1, n):
                if j - i + 1 > max_len and s[i:j + 1] == s[i:j + 1][::-1]:
                    max_len = j - i + 1
                    res = s[i:j + 1]

        return res