from typing import List

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row, col = [0] * len(picture), [0] * len(picture[0])
        result = 0

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    row[i] += 1
                    col[j] += 1

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    if row[i] == 1 and col[j] == 1:
                        result += 1

        return result


