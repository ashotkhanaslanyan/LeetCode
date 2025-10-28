import pytest
from solutions.problem_1486_xor_operation_in_an_array.solution import Solution

solver = Solution()

@pytest.mark.parametrize("n, start, expected", [
    (5, 0, 8),
    (4, 3, 8),
    (1, 7, 7),
    (10, 5, 2),
    (0, 0, 0),
])
def test_xor_operation(n, start, expected):
    assert solver.xorOperation(n, start) == expected