class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cost = [[0] * (n + 1) for _ in range(n + 1)]

        for end in range(2, n + 1):
            for start in range(end - 1, 0, -1):
                minCost = float('inf')
                for i in range(start, end):
                    minCost = min(max(cost[start][i - 1], cost[i + 1][end]) + i, minCost)
                    cost[start][end] = minCost
        print(cost)
        return cost[1][n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.getMoneyAmount(10))

