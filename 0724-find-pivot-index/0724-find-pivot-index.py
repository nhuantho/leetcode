class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            l, r = 0, 0
            if i == 0:
                l = 0
            else:
                l = sum(nums[0:i])
            if i == n - 1:
                r = 0
            else:
                r = sum(nums[i+1:n])
            
            if l == r:
                return i
        return -1
