class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            step_1 = int(s[i - 1])
            step_2 = int(s[i - 2:i])

            if step_1 >= 1 and step_1 <= 9:
                dp[i] += dp[i - 1]
            if step_2 >= 10 and step_2 <= 26:
                dp[i] += dp[i - 2]

        return dp[n]