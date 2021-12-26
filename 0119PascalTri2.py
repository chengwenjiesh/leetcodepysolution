from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev = [1]
        for i in range(1, rowIndex + 1):
            curr = prev
            for j in range(i - 1, 0, -1):
                curr[j] += curr[j - 1]
            curr.append(1)
            prev = curr

        return curr

