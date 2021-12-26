from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        result = 0
        candidates = []
        heights.append(0)

        # what is tha possible largest rect you can ending this height?
        # monotnic non-decreasing stack
        for idx, height in enumerate(heights):
            curr = height

            while candidates and curr < candidates[-1][1]:
                prev = candidates.pop()
                left = 0
                if candidates:
                    left = candidates[-1][0] + 1
                result = max(result, (idx - left) * prev[1])

            candidates.append([idx, height])

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea([2,1,5,6,4,3]))

