from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points
        if k <= 0:
            return []

        return self.quickSelect(points, 0, len(points) - 1, k)


    def quickSelect(self, points, start, end, k):
        idx = self.partition(points, start, end)
        if idx == k - 1:
            return points[:k]
        elif idx > k - 1:
            return self.quickSelect(points, start, idx - 1, k)
        else:
            return self.quickSelect(points, idx + 1, end, k)


    def partition(self, points, start, end):
        if start == end:
            return start

        pivot = points[end]
        left = start
        for i in range(start, end):
            if self.cmpDistance(points[i], pivot) < 0:
                points[i], points[left] = points[left], points[i]
                left += 1
        # on the left side of idx 'left', all numbers are greater than pivot
        points[left], points[end] = points[end], points[left]
        return left

    def cmpDistance(self, pt1, pt2):
        return pt1[0] ** 2 + pt1[1] ** 2 - pt2[0] ** 2 - pt2[1] ** 2

