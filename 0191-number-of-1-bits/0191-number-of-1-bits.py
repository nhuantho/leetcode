class Solution:
    def hammingWeight(self, n: int) -> int:
        list_binary = [0] * 32
        cnt = 31
        while n > 0:
            list_binary[cnt] = n % 2
            cnt -= 1
            n //= 2

        return sum(list_binary)