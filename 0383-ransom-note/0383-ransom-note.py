class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
         
        if len(ransomNote) > len(magazine):
            return False
        
        s_r = set(ransomNote)

        for s in s_r:
            if ransomNote.count(s) > magazine.count(s):
                return False
        
        return True
        