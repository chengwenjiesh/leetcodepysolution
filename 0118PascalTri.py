from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        prev = [1]
        result = [[1]]

        for i in range(1, numRows):
            curr = prev
            for j in range(i - 1, 0, -1):
                curr[j] += curr[j - 1]
            curr.append(1)
            result.append(curr[:])
            prev = curr

        return result


