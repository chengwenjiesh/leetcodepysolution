class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []

        result = [[0] * n for _ in range(n)]
        u, d, l, r = 0, n - 1, 0, n - 1
        num = 1

        while u <= d and l <= r:
            for i in range(l, r + 1):
                result[u][i] = num
                num += 1
            u += 1

            for j in range(u, d + 1):
                result[j][r] = num
                num += 1
            r -= 1

            for i in range(r, l - 1, -1):
                result[d][i] = num
                num += 1
            d -= 1

            for j in range(d, u - 1, -1):
                result[j][l] = num
                num += 1
            l += 1
        return result

