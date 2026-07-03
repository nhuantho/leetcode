class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_v = 0
        while l < r:
            max_v = max(min(height[r], height[l]) * (r - l), max_v)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return max_v
        