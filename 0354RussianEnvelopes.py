from typing import List

class Solution:
    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        sortedEnve = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        size = len(envelopes)

        lis = [1] * size
        result = 1
        for i in range(size):
            for j in range(i):
                if sortedEnve[i][1] > sortedEnve[j][1]:
                    lis[i] = max(lis[j] + 1, lis[i])

        return max(lis)

    def maxEnvelopes(self, envelopes):
        sortedEnve = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        size = len(envelopes)

        lis = []
        for i in range(size):
            width = sortedEnve[i][1]
            idx = bisect.bisect_left(lis, width)
            if idx == len(lis):
                lis.append(width)
            else:
                lis[idx] = width

        return len(lis)


