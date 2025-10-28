class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        uglyPrimes: list = [2, 3, 5]
        for prime in uglyPrimes:
            while n%prime == 0:
                n /= prime
        if n == 1:
            return True
        return False