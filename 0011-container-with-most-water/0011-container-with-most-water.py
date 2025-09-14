class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            res = max(min(height[l], height[r]) * (r - l), res)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res