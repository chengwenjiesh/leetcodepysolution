class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = self.getSquareNum(n)
        return False


    def getSquareNum(self, n):
        result = 0
        while n > 0:
            digit = n % 10
            result += (digit ** 2)
            n //= 10
        return result


