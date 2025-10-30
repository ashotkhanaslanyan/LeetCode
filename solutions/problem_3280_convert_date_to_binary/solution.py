class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = bin(int(date[:4]))[2:]
        month = bin(int(date[5:7]))[2:]
        day = bin(int(date[-2:]))[2:]
        return f"{year}-{month}-{day}"
