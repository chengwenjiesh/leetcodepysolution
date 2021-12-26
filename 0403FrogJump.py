from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if 1 not in stones:
            return False
        if len(stones) < 2:
            return True

        s = len(stones)
        path = [[False] * s for _ in range(s + 1)]
        
        path[2][1] = True
        # x axis -> current stone
        # y axis -> how many units in last jump
        for i in range(1, s + 1):
            for j in range(0, s):
                if path[i][j]:
                    k = i - 1 
                    curr = stones[k]
                    if curr + j in stones:
                        path[stones.index(curr + j) + 1][j] = True
                    if curr + j + 1 in stones:
                        path[stones.index(curr + j + 1) + 1][j + 1] = True
                    if curr + j - 1 in stones:
                        path[stones.index(curr + j - 1) + 1][j - 1] = True

        return any(path[-1][j] for j in range(s))


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCross([0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]))
    print(sol.canCross([0,1,2147483647]))
    print(sol.canCross([0,1,3,5,6,8,12,17]))
    print(sol.canCross([0,1,2,3,4,8,9,11]))
