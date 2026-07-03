class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        l = 0
        merge_word = ""
        end = ""
        if m > n:
            end = word1[n:m]
            l = n
        else:
            end = word2[m:n]
            l = m
        
        for i in range(l):
            merge_word = merge_word + word1[i] + word2[i]
        
        return merge_word + end
        

        