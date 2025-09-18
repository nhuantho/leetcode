class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        tmp_res = set()
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s <= 0:
                    if s == 0:
                        tmp_res.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif s > 0:
                    r -= 1
        res = []
        for tmp in tmp_res:
            res.append(list(tmp))
        res.sort()
        return res
        
        