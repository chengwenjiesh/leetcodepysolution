from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        water = []
        lMax = 0
        rMax = 0
        result = 0

        for i in range(size):
            water.append(lMax)
            lMax = max(lMax, height[i])

        for i in range(size - 1, -1, -1):
            water[i] = min(rMax, water[i])
            result += max(0, water[i] - height[i])
            rMax = max(rMax, height[i])

        return result


if __name__ == '__main__':
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

