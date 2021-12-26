class Solution:
    def merge(self, intervals):
        result = []

        for interval in sorted(intervals, key=lambda i: i[0]):
            if result and interval[0] <=result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
