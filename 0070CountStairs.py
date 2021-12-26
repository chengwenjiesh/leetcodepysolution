class Solution:
    def climbStairs2(self, n: int) -> int:
        # keep a list of used steps
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]

    def climbStairs(self, n):
        # n will be at least 1
        if n < 2:
            return 1

        one_behind = 1
        two_behind = 1
        curr_steps = 0

        for i in range(2, n + 1):
            curr_steps = two_behind + one_behind
            two_behind = one_behind
            one_behind = curr_steps

        return curr_steps


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(10))
