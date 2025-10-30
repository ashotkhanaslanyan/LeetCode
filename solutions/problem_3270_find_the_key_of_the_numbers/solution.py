class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        first: int = min(num1//1000, num2//1000, num3//1000)
        num1, num2, num3 = num1%1000, num2%1000, num3%1000
        second: int = min(num1//100, num2//100, num3//100)
        num1, num2, num3 = num1%100, num2%100, num3%100
        third: int = min(num1//10, num2//10, num3//10)
        num1, num2, num3 = num1%10, num2%10, num3%10
        forth: int = min(num1, num2, num3)
        return 1000 * first + 100 * second + 10 * third + forth