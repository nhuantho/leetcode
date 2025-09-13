class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)

        longest_consecutive_number = 1

        for num in nums:
            if num - 1 not in nums:
                next_num = num + 1
                while next_num in nums:
                    next_num = next_num + 1
                longest_consecutive_number = max(longest_consecutive_number, next_num - num)

        return longest_consecutive_number