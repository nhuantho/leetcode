class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        fib_sequence = [0] * (n + 1)
        fib_sequence[1] = 1
        fib_sequence[2] = 1

        for i in range(3, n + 1):
            fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]

        return fib_sequence[n]