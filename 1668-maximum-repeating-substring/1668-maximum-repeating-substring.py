class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        len_s = len(sequence)
        len_w = len(word)
        if len_s == 0 or len_w == 0:
            return 0
        if sequence == word:
            return 1
        dp = [0] * (len_s + 1)

        for i in range(len_w, len_s + 1):
            print(sequence[i - len_w: i])
            if word == sequence[i - len_w: i]:
                dp[i] = dp[i - len_w] + 1
        return max(dp)