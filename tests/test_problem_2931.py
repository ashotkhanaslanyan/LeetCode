import pytest
from solutions.problem_2931_maximum_spending_after_buying_items.solution import Solution

solver = Solution()

@pytest.mark.parametrize("values, expected", [
    ([[8,5,2],[6,4,1],[9,7,3]], 285),
    ([[5,5,5],[5,5,5],[5,5,5]], 225),
])
def test_max_spending(values, expected):
    assert solver.maxSpending(values) == expected