class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k]) / k
        res = total
        for i in range(k, len(nums)):
            total = (total * k - nums[i - k] + nums[i]) / k
            res = max(total, res)
        return res