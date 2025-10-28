from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        strongest_xor: int = 0
        nums.sort()
        for index, i in enumerate(nums):
            for j in nums[index+1:]:
                if abs(i - j) <= min(i, j):
                    strongest_xor = max(strongest_xor, i^j)
                else:
                    break
        return strongest_xor
