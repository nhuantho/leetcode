class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = dict()
        d_t = dict()

        for i in s:
            if i in d_s:
                d_s.update({i:d_s[i] + 1})
            else:
                d_s.update({i:1})
        
        for i in t:
            if i in d_t:
                d_t.update({i:d_t[i] + 1})
            else:
                d_t.update({i:1})
        
        for k, v in d_s.items():
            if d_t.get(k) != v:
                return False
        for k, v in d_t.items():
            if d_s.get(k) != v:
                return False
        return True

        