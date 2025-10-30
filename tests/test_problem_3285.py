import pytest
from solutions.problem_3285_find_indices_of_stable_mountains.solution import Solution

solver = Solution()

@pytest.mark.parametrize("height, threshold, expected", [
    ([1, 2, 3, 4, 5], 2, [3, 4]),
    ([10, 1, 10, 1, 10], 3, [1, 3]),
    ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4]),
])
def test_stable_mountains(height, threshold, expected):
    assert solver.stableMountains(height, threshold) == expected
