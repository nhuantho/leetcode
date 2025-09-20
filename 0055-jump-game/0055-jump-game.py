class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        furtherest = 0
        for i in range(n):
            if i > furtherest:
                continue
            furtherest = max(furtherest, i + nums[i])
            if furtherest >= n - 1:
                return True
        return False
