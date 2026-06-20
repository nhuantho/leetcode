class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        s_set = set()

        while True:
            n_tmp = 0
            for i in n_str:
                n_tmp += int(i)**2
            
            if n_tmp == 1:
                return True
            
            if n_tmp in s_set:
                return False
            
            s_set.add(n_tmp)
            
            n_str = str(n_tmp)

        