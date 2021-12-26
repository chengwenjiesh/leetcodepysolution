class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [[0] * size for _ in range(size)]

        for end in range(size):
            dp[end][end] = 1
            for start in range(end - 1, -1, -1):
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

        return dp[0][size - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindromeSubseq("abcbaa"))

