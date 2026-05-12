class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split(" ")
        s = pattern
        memo = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in memo:
                memo[s_char] = t_char
            elif memo[s_char] != t_char:
                return False

        map_values = set()

        for v in memo.values():
            if v in map_values:
                return False
            else:
                map_values.add(v)

        return True