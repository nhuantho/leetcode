class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        len_r, len_m = len(ransomNote), len(magazine)

        ransomNote =  "".join(sorted(ransomNote))
        magazine =  "".join(sorted(magazine))
         
        if len_r > len_m:
            return False
        
        memo = []

        i, j = 0, 0
        
        while i < len_r and j < len_m:
            if ransomNote[i] == magazine[j]:
                memo.append(ransomNote[i])
                i+=1
                j+=1
            else:
                j+=1
        
        if len(memo) == len_r:
            return True
        
        return False
        