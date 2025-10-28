import pytest
from solutions.problem_2614_prime_in_diagonal.solution import Solution

solver = Solution()

@pytest.mark.parametrize("nums, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 7),
    ([[1, 10], [4, 5]], 5),
    ([[3, 2, 1, 1], [5, 2, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1]], 3),
    ([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 3, 6], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], 5),
])
def test_diagonal_prime(nums, expected):
    assert solver.diagonalPrime(nums) == expected