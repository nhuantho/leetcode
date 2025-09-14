class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def expand_around_center(l, r):
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

            return cnt

        for i in range(0, n):
            odd = expand_around_center(i, i)
            even = expand_around_center(i, i + 1)
            res = res + odd + even

        return res