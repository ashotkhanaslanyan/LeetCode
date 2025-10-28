import pytest
from solutions.problem_495_teemo_attacking.solution import Solution

solver = Solution()

@pytest.mark.parametrize("timeSeries, duration, expected", [
    ([1, 4], 2, 4),
    ([1, 2], 2, 3),
    ([1, 5, 10], 3, 9),
    ([1], 5, 5),
    ([1, 2, 3, 4, 5], 1, 5),
])
def test_find_poisoned_duration(timeSeries, duration, expected):
    assert solver.findPoisonedDuration(timeSeries, duration) == expected