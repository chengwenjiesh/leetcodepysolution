from typing import List

class Solution:
    def findMaxForm2D(self, strs: List[str], m: int, n: int) -> int:
        sz = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(sz + 1)]
        result = 0

        for i in range(1, sz + 1):
            zero, one = strs[i - 1].count('0'), strs[i - 1].count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zero and k >= one:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zero][k - one] + 1)
                        result = max(result, dp[i][j][k])
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return result


    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        sz = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        result = 0

        for i in range(1, sz + 1):
            zero, one = strs[i - 1].count('0'), strs[i - 1].count('1')
            for j in range(m, zero - 1, -1):
                for k in range(n, one - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zero][k - one] + 1)
                    result = max(result, dp[j][k])

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxForm(["10","0001","111001","1","0"],5,3))

