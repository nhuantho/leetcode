class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiouAEIOU")
        c_prev, i_prev = s[0], 0
        total_vowels = 0
        for c in s[0:k]:
            if c in vowels:
                total_vowels += 1

        res = total_vowels
        for i in range(k, len(s)):
            if c_prev in vowels:
                total_vowels -= 1

            if s[i] in vowels:
                total_vowels += 1
            
            i_prev += 1
            c_prev = s[i_prev]

            res = max(res, total_vowels)

        return res