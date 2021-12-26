from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)
        currMax = gMax = currMin = gMin = nums[0]
        numSum = sum(nums)

        for i in range(1, size):
            currMax = currMax + nums[i] if currMax > 0 else nums[i]
            gMax = max(currMax, gMax)

        for j in range(1, size):
            currMin = currMin + nums[j] if currMin < 0 else nums[j]
            gMin = min(currMin, gMin)

        return gMax if gMax < 0 else max(gMax, numSum - gMin)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubarraySumCircular([5,-3,5]))

