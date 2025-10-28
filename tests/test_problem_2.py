import pytest
from solutions.problem_2_add_two_numbers.solution import Solution
from helpers.ListNode import create_linked_list, linked_list_to_list


solver = Solution()


@pytest.mark.parametrize("l1_list, l2_list, expected_list", [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ([], [1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [], [1, 2, 3]),
    ([5], [5], [0, 1]),
])
def test_add_two_numbers(l1_list, l2_list, expected_list):
    l1 = create_linked_list(l1_list)
    l2 = create_linked_list(l2_list)
    result_node = solver.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result_node)
    assert result_list == expected_list