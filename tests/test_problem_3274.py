import pytest
from solutions.problem_3274_check_if_two_chessboard_squares_have_the_same_color.solution import Solution

solver = Solution()

@pytest.mark.parametrize("coordinate1, coordinate2, expected", [
    ("A1", "B2", True),
    ("C3", "D4", True),
    ("E5", "F6", True),
    ("G7", "H8", True),
    ("A1", "H7", False),
])
def test_check_two_chessboards(coordinate1, coordinate2, expected):
    assert solver.checkTwoChessboards(coordinate1, coordinate2) == expected
