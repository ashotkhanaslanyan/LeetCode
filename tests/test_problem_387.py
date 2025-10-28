import pytest
from solutions.problem_387_first_unique_character_in_a_string.solution import Solution

solver = Solution()

@pytest.mark.parametrize("s, expected", [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
])
def test_first_unique_character(s, expected):
    assert solver.firstUniqChar(s) == expected