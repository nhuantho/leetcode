class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1, d2 = dict(), dict()
        for i in word1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        for i in word2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        
        d1_v = list(d1.values())
        d2_v = list(d2.values())
        d1_v.sort()
        d2_v.sort()

        check = True
        
        if set(d1.keys()) != set(d2.keys()):
            return False

        if len(d1_v) == len(d2_v):
            for i in range(len(d2_v)):
                if d1_v[i] != d2_v[i]:
                    return False
        else:
            return False
            
        return True
        