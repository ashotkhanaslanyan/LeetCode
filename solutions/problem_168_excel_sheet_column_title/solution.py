class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result: str = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result = chr(ord('A') + remainder) + result
        return result
