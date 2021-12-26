class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        sz = len(s)
        dp = [[False] * sz for _ in range(sz)]
        cnt = 0

        for end in range(sz):
            for start in range(end, -1, -1):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                        dp[start][end] = True
                        cnt += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings("aaa"))

