class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        height = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            result = max(result, self.largestRectangleArea(height))

        return result


    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        result = 0
        candidates = []
        heights.insert(0, 0)
        heights.append(0)

        # use stack to store highest bar you may have to form rect
        for idx in range(len(heights)):
            curr = heights[idx]
            while candidates and curr < heights[candidates[-1]]:
                prev = candidates.pop()
                left = candidates[-1] + 1
                result = max(result, (idx - left) * heights[prev])
            candidates.append(idx)

        return result

