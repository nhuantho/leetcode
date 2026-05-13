class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            tmp = s.copy()
            s[n-i-1]=tmp[i]
            s[i]=tmp[n-i-1]
        
        