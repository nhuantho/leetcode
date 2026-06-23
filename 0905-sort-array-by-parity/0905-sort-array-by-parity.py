class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, 1

        if nums[i] % 2 == 0:
            j += 1
            i += 1

        while j < n:
            if nums[j] % 2 == 0:
                k = j
                while k > i:
                    nums[k], nums[k - 1] = nums[k - 1], nums[k]
                    k -= 1

                i += 1

            j += 1
        
        return nums