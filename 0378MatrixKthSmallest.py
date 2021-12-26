from typing import List
import heapq

class Solution:
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        # 1 <= k <= n * n
        n = len(matrix)
        visited = [[False] * n for i in range(n)]
        min_heap = [(matrix[0][0], 0, 0)]

        while k:
            # populate smallest element
            # expand its neighbour into pq
            (result, row, col) = heapq.heappop(min_heap)

            if row < n - 1 and not visited[row + 1][col]:
                heapq.heappush(min_heap, (matrix[row + 1][col], row + 1, col))
                visited[row + 1][col] = True
            if col < n - 1 and not visited[row][col + 1]:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
                visited[row][col + 1] = True

            k -= 1

        return result

    def kthSmallest(self, matrix, k):
        # 1 <= k <= m * n
        m, n = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[m - 1][n - 1]
        candidate = float('-inf')

        while low <= high:
            mid = low + (high - low) // 2
            if self.countLessOrEqual(matrix, mid) >= k:
                candidate = mid
                high = mid - 1
            else:
                low = mid + 1

        return candidate

    def countLessOrEqual(self, matrix, num):
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        cnt = 0

        for row in range(m):
            while col >= 0 and matrix[row][col] > num:
                col -= 1
            cnt += (col + 1)

        return cnt


if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    print(sol.kthSmallest(matrix,8))
    print(sol.kthSmallest1(matrix,8))
