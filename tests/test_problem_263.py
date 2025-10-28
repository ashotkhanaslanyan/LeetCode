import pytest
from solutions.problem_263_ugly_number.solution import Solution

solver = Solution()


@pytest.mark.parametrize("n, expected", [
    (6, True),
    (1, True),
    (14, False),
    (0, False),
    (-1, False),
    (8, True),
    (30, True),
    (11, False),
])
def test_is_ugly(n, expected):
    assert solver.isUgly(n) == expected
