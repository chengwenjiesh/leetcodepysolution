from typing import List

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        size = len(nextVisit)
        firstDays = [0] * size

        for i in range(1, size):
            firstDays[i] = (firstDays[i - 1] + 1 + \
                           (firstDays[i - 1] - firstDays[nextVisit[i - 1]]) + 1) % (10 ** 9 + 7)

        return firstDays[size - 1]


