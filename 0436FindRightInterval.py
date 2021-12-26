from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        size = len(intervals)
        for i in range(size):
            intervals[i].append(i)

        itvlSorted = sorted(intervals)
        result = []

        for i in intervals:
            end = i[1]
            l, r = 0, size - 1
            while l < r:
                mid = l + (r - l) // 2
                if itvlSorted[mid][0] < end:
                    l = mid + 1
                else:
                    r = mid
            if itvlSorted[l][0] < end:
                result.append(-1)
            else:
                result.append(itvlSorted[l][2])

        return result


