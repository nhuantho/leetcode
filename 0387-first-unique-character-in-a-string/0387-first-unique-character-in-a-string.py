class Solution:
    def firstUniqChar(self, s: str) -> int:
        d_s = {}
        for i in range(len(s)):
            if s[i] in d_s:
                d_s[s[i]][0] = d_s[s[i]][0] + 1
            else:
                d_s[s[i]] = [1, i]
        min_index = 10**9
        for k, v in d_s.items():
            if v[0] == 1:
                min_index = min(min_index, v[1])
        
        if min_index == 10**9:
            return -1
        else:
            return min_index



        