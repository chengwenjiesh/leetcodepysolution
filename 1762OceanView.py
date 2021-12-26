from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        nextHigher = [heights[-1]]
        result = [len(heights) - 1]

        for i in range(len(heights) - 2, -1, -1):
            while nextHigher and nextHigher[-1] < heights[i]:
                nextHigher.pop()
            if not nextHigher:
                result.append(i)
            nextHigher.append(heights[i])

        return result[::-1]


