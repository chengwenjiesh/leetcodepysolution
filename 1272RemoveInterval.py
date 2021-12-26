from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]):
        l, r = toBeRemoved[0], toBeRemoved[1]
        result = []
        for itvl in intervals:
            start, end = itvl[0], itvl[1]
            if start >= r or end <= l:
                result.append([start, end])
            else:
                if start < l:
                    result.append([start, l])
                if end > r:
                    result.append([r, end])

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeInterval([[0,5]],[2,3]))

