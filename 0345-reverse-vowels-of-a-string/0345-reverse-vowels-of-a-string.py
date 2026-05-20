class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        n = len(s)
        i, j = 0, n -1

        new_s = [c for c in s]

        while i < j:
            if new_s[i] in vowels and new_s[j] in vowels:
                new_s[i], new_s[j] = new_s[j], s[i]
                i+=1
                j-=1
            
            if new_s[i] not in vowels:
                i += 1
            if new_s[j] not in vowels:
                j-=1
        return "".join(new_s)