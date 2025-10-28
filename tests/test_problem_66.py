import pytest
from solutions.problem_66_plus_one.solution import Solution

solver = Solution()

@pytest.mark.parametrize("digits, expected", [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([0], [1]),
    ([9], [1, 0]),
])
def test_plus_one(digits, expected):
    assert solver.plusOne(digits) == expected