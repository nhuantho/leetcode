class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max, res = 0, -99999999999
        for i in nums:
            current_max = max(i, current_max + i)
            res = max(res, current_max)
        return res