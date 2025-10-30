import pytest
from solutions.problem_3270_find_the_key_of_the_numbers.solution import Solution

solver = Solution()

@pytest.mark.parametrize("num1, num2, num3, expected", [
    (1234, 2345, 3456, 1234),
    (9876, 8765, 7654, 7654),
    (1111, 2222, 3333, 1111),
    (0, 0, 0, 0),
    (999, 888, 777, 777),
])
def test_generate_key(num1, num2, num3, expected):
    assert solver.generateKey(num1, num2, num3) == expected
