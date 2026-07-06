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
        
        if set(d1.keys()) != set(d2.keys()):
            return False
        d1_v = list(d1.values())
        d2_v = list(d2.values())
        if len(d1_v) == len(d2_v):
            d1_v_d, d2_v_d = dict(), dict()
            for i in d1_v:
                if i in d1_v_d:
                    d1_v_d[i] += 1
                else:
                    d1_v_d[i] = 1
            
            for i in d2_v:
                if i in d2_v_d:
                    d2_v_d[i] += 1
                else:
                    d2_v_d[i] = 1

            for i in d1_v_d:
                if i not in d2_v_d or d1_v_d[i] != d2_v_d[i]:
                    return False
        else:
            return False

        return True
        