class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(2, n + 1):
            next_fib = a + b
            a = b
            b = next_fib
        return b