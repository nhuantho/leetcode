class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        n = len(s)

        def expand_around_center(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r]

        res = s[0]
        for i in range(0, n):
            odd = expand_around_center(i, i)
            even = expand_around_center(i, i + 1)

            if len(odd) > len(res):
                res = odd

            if len(even) > len(res):
                res = even

        return res