class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start_pos = set()
        start_pos.add(0)
        n = len(nums)
        for i in range(1, n):
            if nums[i] == 1 and nums[i - 1] == 0:
                start_pos.add(i)
        
        res = 0
        for start in start_pos:
            tmp_k = k
            i = start
            total_one = 0
            while i < n:
                if nums[i] == 0:
                    tmp_k -= 1
                
                if tmp_k < 0:
                    break
                
                total_one += 1
                i += 1
            if tmp_k > 0:
                total_one += tmp_k
                if total_one > n:
                    total_one = n
            res = max(total_one, res)
        
        return res

                    

            
        