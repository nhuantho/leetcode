class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        visited = dict()
        for i in range(n):
            visited.update({nums[i]: i})
        res = []
        for i in range(n - 2):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            j = i + 1
            while j < n - 1:
                if (0 - (nums[i] + nums[j])) in visited and visited[0 - (nums[i] + nums[j])] > j:
                    res.append([nums[i], nums[j], 0 - (nums[i] + nums[j])])
                    if visited[0 - (nums[i] + nums[j])] < j:
                        break
                j += 1
                while nums[j] == nums[j - 1] and j < n -1:
                    j += 1
        return res