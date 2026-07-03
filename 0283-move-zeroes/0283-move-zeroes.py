class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for i in range(index, n):
            nums[i] = 0
        