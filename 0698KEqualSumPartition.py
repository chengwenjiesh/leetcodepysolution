from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numSum = sum(nums)

        if numSum % k:
            return False
        used = [False] * len(nums)
        return self.canPartition(nums, numSum / k, used, 0, 0, k)

    def canPartition(self, nums, target, used, startIdx, currSum, k):
        if k == 1:
            return True

        if currSum > target:
            return False

        if currSum == target:
            return self.canPartition(nums, target, used, 0, 0, k - 1)

        for i in range(startIdx, len(nums)):
            if not used[i]:
                used[i] = True
                if self.canPartition(nums, target, used, i, currSum + nums[i], k):
                    return True
                used[i] = False

        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartitionKSubsets([4,1,2,3,5,3,2], 4))
