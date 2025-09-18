class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        visited = dict()
        for i in range(n):
            if (target - nums[i]) in visited:
                return [visited[target - nums[i]], i]
            visited.update({nums[i]: i})
        return []