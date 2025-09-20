class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = 0
        list_binary = [0] * 32
        cnt = 31
        while n > 0:
            list_binary[cnt] = n%2
            cnt -= 1
            n //= 2
        print(list_binary)
        len_bin = len(list_binary)
        for i in range(len_bin):
            new_n += list_binary[i] * 2**i
        return new_n