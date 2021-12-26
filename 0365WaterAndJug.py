class Solution:
    def canMeasureWater(self, jug1, jug2, target):
        if jug1 + jug2 < target:
            return False
        return target % self._gcd(jug1, jug2) == 0

    def _gcd(self, a, b):
        while b:
            r = a % b
            a = b
            b = r
        return a

if __name__ == '__main__':
    sol = Solution()
    print(sol.canMeasureWater(3,5,4))

