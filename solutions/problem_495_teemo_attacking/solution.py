from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisonedTime = 0
        if len(timeSeries) == 1:
            return duration
        for index, attack in enumerate(timeSeries):
            attackInterval = attack - timeSeries[index - 1]
            if attackInterval < duration and attackInterval >= 0:
                poisonedTime += duration - (duration - attackInterval)
            else:
                poisonedTime += duration
        return poisonedTime
