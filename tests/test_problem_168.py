import pytest
from solutions.problem_168_excel_sheet_column_title.solution import Solution

solver = Solution()


@pytest.mark.parametrize("columnNumber, expected", [
    (1, "A"),
    (26, "Z"),
    (27, "AA"),
    (28, "AB"),
    (52, "AZ"),
    (701, "ZY"),
    (703, "AAA"),
])
def test_convert_to_title(columnNumber, expected):
    assert solver.convertToTitle(columnNumber) == expected