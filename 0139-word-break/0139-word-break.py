class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        solve_mem = dict()
        def solve(s):
            if len(s) == 0:
                return True
            res = False
            for word in wordDict:
                if s.endswith(word):
                    sub_s = s[0:len(s) - len(word)]
                    res = res or (solve_mem[sub_s] if sub_s in solve_mem else solve(sub_s))
            solve_mem.update({s: res})
            return res
        return solve(s)