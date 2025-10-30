from typing import List

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        result: List[int] = []
        for i in range(len(height) - 1):
            if height[i] > threshold:
                result.append(i+1)
        return result