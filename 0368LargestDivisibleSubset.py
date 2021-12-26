from typing import List

class Solution:
    def largestDivisibleSubset2(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        if sz < 2:
            return nums

        nums.sort()
        dp = [[nums[i]] for i in range(sz)]
        maxLen = 1
        maxSub = [nums[0]]

        for i in range(1, sz):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
                    if len(dp[i]) > len(maxSub):
                        maxSub = dp[i]

        return maxSub

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestDivisibleSubset2([2,3,4,9,8]))

