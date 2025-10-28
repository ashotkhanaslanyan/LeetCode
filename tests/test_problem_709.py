import pytest
from solutions.problem_709_to_lower_case.solution import Solution

solver = Solution()

@pytest.mark.parametrize("input_str, expected_output", [
    ("Hello", "hello"),
    ("here", "here"),
    ("LOVELY", "lovely"),
    ("Python3.8", "python3.8"),
    ("", ""),
    ("12345", "12345"),
    ("MiXeD CaSe", "mixed case"),
])
def test_to_lower_case(input_str, expected_output):
    assert solver.toLowerCase(input_str) == expected_output