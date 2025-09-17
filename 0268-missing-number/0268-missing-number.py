class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in nums:
            dp[i] = 1

        for i in range(1, n + 1):
            if dp[i] == 0:
                return i
        return 0
        