from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.findCombinations(result, [], 1, n, k)
        return result

    def findCombinations(self, result, curr, idx, n, k):
        if not k:
            result.append(curr[:])
            return

        for i in range(idx, n + 1):
            curr.append(i)
            self.findCombinations(result, curr, i + 1, n, k - 1)
            curr.pop()


if __name__ == '__main__':
    sol = Solution()
    result = sol.combine(4, 2)
    print(result)
