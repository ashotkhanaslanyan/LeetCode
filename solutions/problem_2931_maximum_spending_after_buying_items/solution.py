from typing import List

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        item_values: List[int] = []
        max_spending: int = 0
        for shop in values:
            for item in shop:
                item_values.append(item)
        item_values.sort()
        for index, item in enumerate(item_values):
            max_spending += item * (index + 1)
        return max_spending