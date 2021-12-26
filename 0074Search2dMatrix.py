from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # assume matrix is at least 1*1
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid // n][mid % n]
            if mid_value == target:
                return True
            elif mid_value > target:
                right = mid - 1
            else:
                left = mid + 1

        return matrix[left // n][left % n] == target


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
