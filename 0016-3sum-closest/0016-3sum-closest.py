class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        min_sum = 10 ** 5
        res = 0
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                tmp_min_sum = abs(target - tmp_sum)
                if tmp_min_sum < min_sum:
                    min_sum = tmp_min_sum
                    res = tmp_sum

                if tmp_sum < target:
                    j = j + 1
                else:
                    k -= 1

        return res