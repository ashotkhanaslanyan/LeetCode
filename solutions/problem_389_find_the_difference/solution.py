class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charCount: dict = {}
        for char in set(t):
            charCount[char] = s.count(char)
            charCount[char] += t.count(char)
        for key, val in charCount.items():
            if val%2 == 1:
                return key