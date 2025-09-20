class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        furtherest = 0
        jumps = 0
        current_index = 0
        for i in range(n):
            if i > furtherest:
                continue
            furtherest = max(furtherest, i + nums[i])
            if current_index == i:
                current_index = furtherest
                jumps += 1
                if furtherest >= n - 1:
                    return jumps
        return 0