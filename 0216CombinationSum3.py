from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 1:
            return [n] if 1 <= n <= 9 else []

        result = []
        self.findCombination(k, n, [], result)
        return result

    def findCombination(self, k, n, curr, result):
        if k == 0:
            if n == 0:
                result.append(curr[:])
            return

        prev = curr[-1] if curr else 0
        for i in range(prev + 1, 10):
            if n >= i:
                curr.append(i)
                self.findCombination(k - 1, n - i, curr, result)
                curr.pop()


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum3(3,9))

