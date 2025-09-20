class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        dp = [0] * (n + 1)
        for i in range(n):
            if i + nums[i] >= n - 1:
                return dp[i] + 1
            for j in range(i + 1, i + nums[i] + 1):
                if dp[j] == 0:
                    dp[j] = dp[i] + 1

        return 0