import math

class Solution:
    def getFactors(self, n: int):
        if n < 2:
            return []

        result = []
        self.findComb(n, 2, [], result)
        return result

    def findComb(self, n, factor, curr, result):
        if n == 1:
            if len(curr) > 1:
                result.append(curr[:])
            return

        for i in range(factor, int(math.sqrt(n)) + 1):
            if n % i == 0:
                curr.append(i)
                self.findComb(n // i, i, curr, result)
                curr.pop()

        curr.append(n)
        self.findComb(1, n, curr, result)
        curr.pop()

if __name__ == '__main__':
    sol = Solution()
    print(sol.getFactors(12))
    print(sol.getFactors(9174093))

