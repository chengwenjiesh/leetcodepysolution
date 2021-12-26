class Solution:
    def maxSubArray(self, nums):
        currSum = maxSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(currSum, maxSum)

        return maxSum


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([1,4,-1,7,8]))
