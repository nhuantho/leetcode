class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s_nums1 = set(nums1)
        s_nums2 = set(nums2)
        return [list(s_nums1 - s_nums2), list(s_nums2 - s_nums1)]
        