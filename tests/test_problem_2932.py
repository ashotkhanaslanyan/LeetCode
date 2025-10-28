import pytest
from solutions.problem_2932_maximum_strong_pair_xor_i.solution import Solution

solver = Solution()

@pytest.mark.parametrize("nums, expected", [
    ([5, 6, 25, 30], 7),
    ([1, 2, 3, 4, 5], 7),
    ([1, 1], 0),
    ([2, 2, 2], 0),
])
def test_maximum_strong_pair_xor(nums, expected):
    assert solver.maximumStrongPairXor(nums) == expected