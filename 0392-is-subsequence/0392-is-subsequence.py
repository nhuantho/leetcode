class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        if t == "":
            return False

        index_s = 0
        dp = [False] * (len(s))

        for c in t:
            if s[index_s] == c:
                dp[index_s] = True
                index_s += 1
            
            if index_s == len(s):
                break

        return dp[len(s) - 1]