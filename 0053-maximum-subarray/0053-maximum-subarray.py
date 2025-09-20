class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = nums[0]

        for i in range(1, n):
            if res + nums[i] < 0:
                res = max(res, nums[i])
            else:
                res = res + nums[i]
        return res