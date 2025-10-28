import pytest
from solutions.problem_389_find_the_difference.solution import Solution

solver = Solution()


@pytest.mark.parametrize("s, t, expected", [
    ("abcd", "abcde", "e"),
    ("", "y", "y"),
    ("a", "aa", "a"),
    ("ae", "aea", "a"),
])
def test_find_the_difference(s, t, expected):
    assert solver.findTheDifference(s, t) == expected