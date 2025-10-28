from typing import List
from math import floor, sqrt

class Solution:
    def is_prime(self, num: int) -> bool:
        if num == 2:
            return True
        if num < 2:
            return False
        for i in range(2, int(floor(sqrt(num)))+1):
            if num % i == 0:
                return False
        return True


    def diagonalPrime(self, nums: List[List[int]]) -> int:
        diagonal_nums: List[int] = []
        for i in range(len(nums)):
            diagonal_nums.append(nums[i][i])
            diagonal_nums.append(nums[i][len(nums)-1-i])
        diagonal_nums = sorted(set(diagonal_nums))[::-1]
        print(f"Diagonal nums: {diagonal_nums}")
        for num in diagonal_nums:
            if self.is_prime(num):
                return num
        return 0