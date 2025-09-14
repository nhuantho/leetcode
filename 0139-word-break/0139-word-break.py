class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n

        for i in range(n):
            for word in wordDict:
                if s[0:i + 1].endswith(word):
                    if i - len(word) < 0:
                        dp[i] = True
                    else:
                        dp[i] = dp[i] or dp[i - len(word)]
        return dp[n - 1]