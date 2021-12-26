import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, num1, num2, k: int) -> List[List[int]]:
        # num1 and num2 are not empty
        if not num1 or not num2 or not k:
            return []

        minHeap = []
        for i, num in enumerate(num2):
            heapq.heappush(minHeap, (num + num1[0], 0, i))

        result = []
        idx1 = 1

        while k > 0 and minHeap:
            numSum, i, j = heapq.heappop(minHeap)
            result.append([num1[i], num2[j]])
            if i < len(num1) - 1:
                heapq.heappush(minHeap, (num1[i + 1] + num2[j], i + 1, j))
            k -= 1

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.kSmallestPairs([1,4,7], [2,5,8], 5))

