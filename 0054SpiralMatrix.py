from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        if not m or not n:
            return []

        result = []
        u, d, l, r = 0, m - 1, 0, n - 1
        while u <= d and l <= r:
            for i in range(l, r + 1):
                result.append(matrix[u][i])
            u += 1

            for j in range(u, d + 1):
                result.append(matrix[j][r])
            r -= 1

            if u > d:
                break

            for i in range(r, l - 1, -1):
                result.append(matrix[d][i])
            d -= 1

            if l > r:
                break

            for j in range(d, u - 1, -1):
                result.append(matrix[j][l])
            l += 1
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))

