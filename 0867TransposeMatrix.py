from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(matrix[0])):
            newRow = []
            for j in range(len(matrix)):
                newRow.append(matrix[j][i])
            result.append(newRow)

        return result

    def transposeSquare(self, matrix):
        # matrix is square
        sz = len(matrix)
        for i in range(sz):
            for j in range(i + 1, sz):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return

if __name__ == '__main__':
    sol = Solution()
    print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol.transposeSquare(matrix)
    print(matrix)

