class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        if n == 4:
            if sum(nums) == target:
                return [nums]

        nums.sort()
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                x, y = j + 1, n - 1
                while x < y:
                    tmp_sum = nums[i] + nums[j] + nums[x] + nums[y]

                    if tmp_sum == target:
                        res.append([nums[i], nums[j], nums[x], nums[y]])
                        x, y = x + 1, y - 1

                        while x < y and nums[x] == nums[x - 1]:
                            x+=1
                        while y < y and nums[y] == nums[y - 1]:
                            y-=1

                    elif tmp_sum < target:
                        x += 1
                    else:
                        y -= 1

        return res