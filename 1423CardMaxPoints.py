from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k >= len(cardPoints):
            return total

        remain = 0
        for i in range(len(cardPoints) - k):
            remain += cardPoints[i]
        minRemain = remain

        for i in range(len(cardPoints) - k, len(cardPoints)):
            remain += cardPoints[i]
            remain -= cardPoints[i - len(cardPoints) + k]
            minRemain = min(minRemain, remain)

        return total - minRemain

