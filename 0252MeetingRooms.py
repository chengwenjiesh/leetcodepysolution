class Solution:
    def canAttendMeetings2(self, intervals) -> bool:
        latest = []
        intervals.sort(key = lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


    def canAttendMeetings(self, intervals) -> bool:
        latest = []
        for i in sorted(intervals, key = lambda x: x[0]):
            if latest and i[0] < latest[-1][1]:
                return False
            else:
                latest.append(i)

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canAttendMeetings([[0,30],[5,10],[15,20]]))
    print(sol.canAttendMeetings2([[0,30],[5,10],[15,20]]))
