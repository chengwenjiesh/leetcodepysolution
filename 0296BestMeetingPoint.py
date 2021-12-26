from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        x, y = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        x.sort()
        y.sort()
        result = 0
        for k in range((len(x) // 2)):
            result += (x[len(x) - 1 - k] - x[k] + \
                       y[len(x) - 1 - k] - y[k])
            
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
