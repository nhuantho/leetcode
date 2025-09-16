class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = []

        def generate_binary(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            tmp_res = 0
            while (n >= 1):
                tmp_res = tmp_res + n % 2
                n = n // 2
            return tmp_res

        for i in range(0, n + 1):
            res.append(generate_binary(i))
        return res