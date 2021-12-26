from collections import deque

from typing import List

class Solution:
    def sequentialDigitsDFS(self, low: int, high: int) -> List[int]:
        if low > high:
            return []

        result = []
        for i in range(1, 10):
            self.buildSeqInt(high, i, result)

        return [num for num in result if num >= low]

    def buildSeqInt(self, high, curr, result):
        if curr > high:
            return

        result.append(curr)
        if curr % 10 == 9:
            return

        nextCandidate = curr * 10 + (curr % 10) + 1
        self.buildSeqInt(high, nextCandidate, result)
        return

    def sequentialDigits(self, low, high):
        if low > high:
            return []

        result = []
        q = deque([i for i in range(1,10)])

        while q:
            n = q.popleft()

            if n % 10 != 9:
                candidate = n * 10 + n % 10 + 1
                if candidate <= high:
                    q.append(candidate)

            if n >= low:
                result.append(n)

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.sequentialDigitsDFS(10,1000))
    print(sol.sequentialDigits(10,1000))

