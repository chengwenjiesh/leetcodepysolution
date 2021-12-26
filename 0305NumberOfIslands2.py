from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        islandUF = DSU()
        result = []

        for p in positions:
            if tuple(p) not in islandUF.parents:
                islandUF.add(tuple(p))
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (p[0] + i, p[1] + j) in islandUF.parents:
                        islandUF.union(tuple(p), (p[0] + i, p[1] + j))
            result.append(islandUF.size)

        return result


class DSU:
    # no optimization for size and rank
    def __init__(self):
        self.parents = {}
        self.size = 0

    def add(self, x):
        self.parents[x] = x
        self.size += 1

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xPar, yPar = self.find(x), self.find(y)
        if xPar == yPar:
            return
        else:
            self.parents[xPar] = self.find(yPar)
            self.size -= 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1],[1,1]]))


