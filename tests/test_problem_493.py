import pytest
from solutions.problem_493_construct_the_rectangle.solution import Solution

solver = Solution()

@pytest.mark.parametrize("area, expected", [
    (4, [2, 2]),
    (37, [37, 1]),
    (122122, [427, 286]),
])
def test_construct_rectangle(area, expected):
    assert solver.constructRectangle(area) == expected