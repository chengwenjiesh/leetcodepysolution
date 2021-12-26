from typing import List
import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        size = len(blacklist)
        self.alternative = {}
        self.range = n - size
        blacklist.sort()
        blackset = set(blacklist)

        idx = self.range
        for i in range(size):
            if blacklist[i] < self.range:
                while idx in blackset:
                    idx += 1
                self.alternative[blacklist[i]] = idx
                idx += 1

    def pick(self) -> int:
        idx = random.randint(0, self.range - 1)
        return idx if idx not in self.alternative else self.alternative[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
if __name__ == '__main__':
    sol = Solution(3, [0])
    print(sol.pick())


