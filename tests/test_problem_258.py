import pytest
from solutions.problem_258_add_digits.solution import Solution

solver = Solution()

@pytest.mark.parametrize("num, expected", [
    (38, 2),
    (0, 0),
    (9, 9),
    (10, 1),
    (1, 1),
    (11, 2),
    (12, 3),
    (13, 4),
    (14, 5),
])
def test_add_digits(num, expected):
    assert solver.addDigits(num) == expected