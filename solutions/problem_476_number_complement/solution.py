class Solution:
    def findComplement(self, num: int) -> int:
        binNum: str = bin(num)[2:]
        inverseHash: dict = str.maketrans({'0': '1', '1': '0'})
        inverseNum: str = binNum.translate(inverseHash)
        return int(inverseNum, 2)