from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # [x1, y1, x2, y2]
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and \
               rec1[1] < rec2[3] and rec2[1] < rec1[3]

