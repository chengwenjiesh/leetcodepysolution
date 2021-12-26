from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if len(events) == 0:
            return 0

        events.sort()
        result = curr = idx = 0
        minheap = []

        while idx < len(events) or minheap:
            if not minheap:
                curr = events[idx][0]

            while idx < len(events) and events[idx][0] <= curr:
                heapq.heappush(minheap, events[idx][1])
                idx += 1

            heapq.heappop(minheap)
            result += 1
            curr += 1

            while minheap and minheap[0] < curr:
                heapq.heappop(minheap)

        return result


