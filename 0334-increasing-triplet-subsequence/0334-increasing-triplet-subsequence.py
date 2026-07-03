class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = 2**31
        first = INF
        second = INF

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False