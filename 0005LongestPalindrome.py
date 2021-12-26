class Solution:
    def longestPalindrome(self, s: str) -> str:
        sz = len(s)
        dp = [[False] * sz for _ in range(sz)]
        result = ''

        for end in range(sz):
            for start in range(end, -1, -1):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    if end - start + 1 > len(result):
                        result = s[start : end + 1]

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('abab'))

