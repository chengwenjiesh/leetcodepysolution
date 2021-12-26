from typing import List
import heapq

class Solution:
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        minHeap = [intervals[0][1]]
        roomCount = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= minHeap[0]:
                # no more room needed
                heapq.heappushpop(minHeap, intervals[i][1])
            else:
                heapq.heappush(minHeap, intervals[i][1])
                roomCount += 1

        return roomCount


    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        rooms = 0

        sz = len(intervals)
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)

        sptr, eptr = 0, 0
        while sptr < sz:
            if start[sptr] >= end[eptr]:
                rooms -= 1
                eptr += 1
            rooms += 1
            sptr += 1

        return rooms


if __name__ == '__main__':
    sol = Solution()
    print(sol.minMeetingRooms([[0,30],[30,40],[20,35]]))
