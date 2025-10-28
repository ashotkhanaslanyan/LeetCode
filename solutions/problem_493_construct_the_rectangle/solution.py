from math import sqrt, floor
from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        page = []
        for i in range(1, floor(sqrt(area))+1):
            if area%i == 0:
                page.append(int(area/i))
                page.append(i)
        return page[-2:]