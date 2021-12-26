class Solution:
    def findTargetSumWaysDFS(self, nums: List[int], target: int) -> int:
        cached = {}
        return self.findAllComb(nums, 0, target, len(nums) - 1, cached)


    def findAllComb(self, nums, currSum, target, idx, cached):
        if (idx, currSum) in cached:
            return cached[(idx, currSum)]

        if idx < 0:
            return 1 if currSum == target else 0

        newSum = self.findAllComb(nums, currSum + nums[idx], target, idx - 1, cached) + \
                self.findAllComb(nums, currSum - nums[idx], target, idx - 1, cached)
        cached[(idx, currSum)] = newSum

        return newSum


    def findTargetSumWays2D(self, nums, target):
        numSum = sum(nums)
        if target > numSum or target < 0 - numSum:
            return 0

        dp = [[0] * (2 * numSum + 1) for _ in range(len(nums))]
        dp[0][nums[0] + numSum] += 1
        dp[0][-nums[0] + numSum] += 1

        for i in range(1, len(nums)):
            for j in range(2 * numSum + 1):
                if dp[i - 1][j] > 0:
                    dp[i][j + nums[i]] += dp[i - 1][j]
                    dp[i][j - nums[i]] += dp[i - 1][j]

        return dp[-1][target + numSum]


    def findTargetSumWays(self, nums, target):
        numSum = sum(nums)
        if target > numSum or target < 0 - numSum:
            return 0

        dp = [0] * (2 * numSum + 1)
        dp[nums[0] + numSum] += 1
        dp[-nums[0] + numSum] += 1

        for i in range(1, len(nums)):
            nextSum = [0] * (2 * numSum + 1)
            for j in range(2 * numSum + 1):
                if dp[j] > 0:
                    nextSum[j + nums[i]] += dp[j]
                    nextSum[j - nums[i]] += dp[j]
            dp = nextSum

        return dp[target + numSum]

