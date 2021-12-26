from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if not stations or startFuel < stations[0][0]:
            return -1

        # dp[i] denotes furthest distance you can travel after i stops
        sz = len(stations)
        dp = [startFuel] + [0 for _ in range(sz)]

        for i in range(sz):
            for j in range(i, -1, -1):
                if dp[j] >= stations[i][0]:
                    dp[j + 1] = max(dp[j + 1], dp[j] + stations[i][1])

        for steps, distance in enumerate(dp):
            if distance >= target:
                return steps

        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.minRefuelStops(100, 50, [[25,30]]))


