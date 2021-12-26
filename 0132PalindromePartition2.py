class Solution:
    def minCut(self, s: str) -> int:
        if len(s) < 2:
            return 0

        sz = len(s)
        dp = [[False] * sz for _ in range(sz)]
        cut = [0] * sz

        for end in range(sz):
            cut[end] = end + 1
            for start in range(end, -1, -1):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    if start == 0:
                        cut[end] = 1
                    else:
                        cut[end] = min(cut[end], cut[start - 1] + 1)

        return cut[-1] - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCut("ab"))

