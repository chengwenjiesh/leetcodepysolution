class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        nearestPow2 = 1
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                result[i] = 1
                nearestPow2 = i
            else:
                result[i] = 1 + result[i - nearestPow2]

        return result

