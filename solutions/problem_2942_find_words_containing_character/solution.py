from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result: List[int] = []
        for index, word in enumerate(words):
            if x in word:
                result.append(index)
        return result