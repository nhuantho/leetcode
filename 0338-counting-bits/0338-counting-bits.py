class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = []
        visited = {}
        def generate_binary(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            tmp_res = 0
            while (n >= 1):
                tmp_res = tmp_res + n % 2
                n = n // 2
                if n in visited:
                    tmp_res = tmp_res + visited[n]
                    break
            return tmp_res

        for i in range(0, n + 1):
            res_i = generate_binary(i)
            visited.update({i: res_i})
            res.append(res_i)
        return res