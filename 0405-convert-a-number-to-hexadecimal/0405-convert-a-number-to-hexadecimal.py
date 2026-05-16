class Solution:
    def toHex(self, num: int) -> str:
        memo = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

        def return_hexadecimal_char(x):
            if x in memo:
                return str(memo[x])
            else:
                return str(x)
        
        if num == 0:
            return "0"

        if 0 < num < 16:
            return return_hexadecimal_char(num)
        
        if num < 0:
            num = 2**32 + num

        res = ""
        while num > 0:
            res = str(return_hexadecimal_char(num % 16)) + res
            num = num // 16

        if num > 0:
            res = res + str(return_hexadecimal_char(num))
        
        return res

        