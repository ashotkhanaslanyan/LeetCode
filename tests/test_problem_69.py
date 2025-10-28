import pytest
from solutions.problem_70_climbing_stairs.solution import Solution

solver = Solution()

@pytest.mark.parametrize("n, expected", [
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (10, 89),
])
def test_climb_stairs(n, expected):
    assert solver.climbStairs(n) == expected