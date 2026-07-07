class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in asteroids:
            if i > 0 or len(res) == 0:
                res.append(i)
            else:
                while res:
                    tmp_v = res.pop()
                    if tmp_v < 0:
                        res.append(tmp_v)
                        res.append(i)
                        break
                    if tmp_v + i < 0:
                        if len(res) == 0:
                            res.append(i)
                            break
                        continue
                    if tmp_v + i > 0:
                        res.append(tmp_v)
                        break
                    if tmp_v + i == 0:
                        break
        return res
        