class RecentCounter:

    def __init__(self):
        self.v = []
        

    def ping(self, t: int) -> int:
        self.v.append(t)
        res = 0
        lb = t - 3000
        for i in self.v:
            if i >= lb and i <= t:
                res += 1
        return res
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)