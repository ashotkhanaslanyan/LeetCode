import pytest
from solutions.problem_3280_convert_date_to_binary.solution import Solution

solver = Solution()

@pytest.mark.parametrize("date, expected", [
    ("2080-02-29", "100000100000-10-11101"),
    ("1900-01-01", "11101101100-1-1"),
])
def test_convert_date_to_binary(date, expected):
    assert solver.convertDateToBinary(date) == expected
