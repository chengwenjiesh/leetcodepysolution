from typing import List
from collections import deque

class Solution:
    def findMaxValueOfEquation1(self, points: List[List[int]], k: int) -> int:
        result = float('-inf')
        minHeap = []
        # (xi - yi, xi)
        for x, y in points:
            while minHeap and x - minHeap[0][1] > k:
                heapq.heappop(minHeap)
            if minHeap:
                result = max(result, -minHeap[0][0] + x + y)
            heapq.heappush(minHeap, (x - y, x))

        return result

    def findMaxValueOfEquation(self, points, k):
        # monotonic decreasing
        q = deque([])
        result = float('-inf')
        for x, y in points:
            print('q=')
            print(q)
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                result = max(result, x + y + q[0][0])
            while q and q[-1][0] <= y - x:
                q.pop()
            q.append((y - x, x))

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxValueOfEquation([[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]], 6))

