import pytest
from solutions.problem_476_number_complement.solution import Solution

solver = Solution()

@pytest.mark.parametrize("num, expected", [
    (5, 2),
    (1, 0),
    (0, 1),
    (10, 5),
    (7, 0),
])
def test_find_complement(num, expected):
    assert solver.findComplement(num) == expected