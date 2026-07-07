class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d_r, d_c = dict(), dict()
        n = len(grid)
        for i in range(n):
            tmp_v = ""
            for j in range(n):
                tmp_v += (str(grid[i][j]) + ",")
            d_r[i] = tmp_v
        
        for i in range(n):
            tmp_v = ""
            for j in range(n):
                tmp_v += (str(grid[j][i]) + ",")
            d_c[i] = tmp_v
        
        res = 0
        for i in range(n):
            for j in range(n):
                if d_r[i] == d_c[j]:
                    res += 1
        return res

