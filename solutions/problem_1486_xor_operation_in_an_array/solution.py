class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        init = 0
        for i in range(start, start + n * 2, 2):
            init ^= i
        return init