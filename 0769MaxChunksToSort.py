from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        currMax, result = -1, 0
        for i, v in enumerate(arr):
            currMax = max(currMax, v)
            if currMax == i:
                result += 1

        return result


