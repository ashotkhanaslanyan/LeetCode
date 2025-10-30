import pytest
from solutions.problem_2942_find_words_containing_character.solution import Solution

solver = Solution()

@pytest.mark.parametrize("words, x, expected", [
    (["hello", "leetcode", "apple"], "e", [0, 1 ,2]),
    (["a", "b", "c"], "z", []),
    (["test", "testing", "tested"], "t", [0, 1, 2]),
    (["abc", "def", "ghi"], "a", [0]),
    (["xyz", "xy", "yz"], "y", [0, 1, 2]),
])
def test_find_words_containing(words, x, expected):
    assert solver.findWordsContaining(words, x) == expected