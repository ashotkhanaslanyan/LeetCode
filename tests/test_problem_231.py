import pytest
from solutions.problem_231_power_of_two.solution import Solution

solver = Solution()

@pytest.mark.parametrize("n, expected", [
    (1, True),
    (16, True),
    (3, False),
    (4, True),
    (5, False),
])
def test_is_power_of_two(n, expected):
    assert solver.isPowerOfTwo(n) == expected