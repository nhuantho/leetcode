class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        n = len(s)
        res = ""
        while n - k > 0:
            if res == "":
                res = s[n - k:n]
            else:
                res = s[n - k:n] + "-" + res
            n -= k

        if n > 0:
            if res == "":
                res = s[:n]
            else:
                res = s[:n] + "-" + res

        return res