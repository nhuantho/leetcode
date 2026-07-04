class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = dict()
        n = len(nums)
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        res = 0
        for num in nums:
            tmp = k - num
            if tmp == num:
                if d[num] > 1:
                    res += 1
                    d[num] -= 2
            elif tmp in d and d[num] > 0 and d[tmp] > 0:
                res += 1
                d[num] -= 1
                d[tmp] -= 1
        return res
        