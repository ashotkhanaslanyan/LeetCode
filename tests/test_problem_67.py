import pytest
from solutions.problem_67_add_binary.solution import Solution

solver = Solution()

@pytest.mark.parametrize("a, b, expected", [
    ("11", "1", "100"),
    ("1010", "1011", "10101"),
])
def test_add_binary(a, b, expected):
    assert solver.addBinary(a, b) == expected