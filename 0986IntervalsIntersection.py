class Solution:
    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList:
            return []

        result = []
        m, n = len(firstList), len(secondList)
        i = j = 0
        while i < m and j < n:
            aLeft, aRight = firstList[i][0], firstList[i][1]
            bLeft, bRight = secondList[j][0], secondList[j][1]

            if aLeft <= bRight and bLeft <= aRight:
                result.append([max(aLeft, bLeft), min(aRight, bRight)])

            if aRight < bRight:
                i += 1
            else:
                j += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    print(firstList)
    print(secondList)
    print(sol.intervalIntersection(firstList, secondList))
