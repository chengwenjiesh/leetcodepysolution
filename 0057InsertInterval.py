from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            idx += 1

        if idx == len(intervals):
            intervals.append(newInterval)
            return intervals

        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            intervals.pop(idx)

        intervals.insert(idx, newInterval)

        return intervals


if __name__ == '__main__':
    sol = Solution()
    print(sol.insert([[2,3],[6,9]], [1,1]))
