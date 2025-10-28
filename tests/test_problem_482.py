import pytest
from solutions.problem_482_license_key_formatting.solution import Solution

solver = Solution()

@pytest.mark.parametrize("s, k, expected", [
    ("5F3Z-2e-9-w", 4, "5F3Z-2E9W"),
    ("2-5g-3-J", 2, "2-5G-3J"),
    ("2-4A0r7-4k", 3, "24-A0R-74K"),
    ("---", 3, ""),
    ("a", 1, "A"),
])
def test_license_key_formatting(s, k, expected):
    assert solver.licenseKeyFormatting(s, k) == expected