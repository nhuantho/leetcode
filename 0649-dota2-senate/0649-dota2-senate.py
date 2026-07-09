class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        cur_c, next_c = [], []
        for i in senate:
            cur_c.append(i)

        res = {"R": "Radiant", "D": "Dire"}

        v_r, v_d = 0, 0
        while True:
            check_ban = False
            for i in cur_c:
                if i == 'R' and v_d > 0:
                    check_ban = True
                    v_d -= 1
                elif i == 'R' and v_d == 0:
                    next_c.append(i)
                    v_r += 1
                elif i == 'D' and v_r > 0:
                    check_ban = True
                    v_r -= 1
                else:
                    next_c.append(i)
                    v_d += 1
            if check_ban == False:
                return res[cur_c[-1]]
            cur_c = next_c.copy()
            next_c = []