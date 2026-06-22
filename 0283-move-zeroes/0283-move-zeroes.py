class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n - 1
        i = n - 2

        if nums[j] == 0:
            j -= 1
            i -= 1

        while i >= 0:
            if nums[i] == 0:
                k = i
                while k < j:
                    nums[k], nums[k + 1] = nums[k + 1], nums[k]
                    k += 1

                j -= 1

            i -= 1