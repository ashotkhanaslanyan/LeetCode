import pytest
from solutions.problem_242_valid_anagram.solution import Solution

solver = Solution()

@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("", "", True),
    ("a", "a", True),
    ("ab", "ba", True),
])
def test_is_anagram(s, t, expected):
    assert solver.isAnagram(s, t) == expected
