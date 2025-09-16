class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if groups[i - 1] != groups[i]:
                dp[i] = 1

        res = []
        for i in range(n):
            if dp[i] != 0:
                res.append(words[i])
        return res