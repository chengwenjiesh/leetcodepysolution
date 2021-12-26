class Solution:
    def canPartition1D(self, nums):
        numSum = sum(nums)
        if numSum % 2:
            return False
        target = numSum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            curr = [False] * (target + 1)
            for i in range(target + 1):
                if dp[i] or (i - num >= 0 and dp[i - num]):
                    curr[i] = True
            dp = curr

        return dp[target]

    def canPartition2D(self, nums):
        numSum = sum(nums)
        if numSum % 2:
            return False

        target = numSum // 2

        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True

        for i in range(len(nums)):
            for j in range(target + 1):
                if dp[i][j] or (j - nums[i] >= 0 and dp[i][j - nums[i]]):
                    dp[i + 1][j] = True

        return dp[len(nums)][target]


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([1,5,11,5]))
    print(sol.canPartition([1,2,5]))
