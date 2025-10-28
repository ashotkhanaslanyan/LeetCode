class Solution:
    def firstUniqChar(self, s: str) -> int:
        setS: list = set(s)
        indexes: list = []
        for char in setS:
            first = s.index(char)
            last = s.rindex(char)
            if first == last:
                indexes.append(first)
        if not indexes:
            return -1
        return min(indexes)