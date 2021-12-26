from typing import List

class Solution:
    def canJumpDP(self, nums: List[int]) -> bool:
        # dp top down
        # O(n^2)
        if not nums:
            return True

        canReach = [False] * len(nums)
        canReach[0] = True

        for i in range(len(nums)):
            if canReach[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < len(nums) and not canReach[i + j]:
                        # early termination
                        if i + j == len(nums) - 1:
                            return True
                        canReach[i + j] = True

        return canReach[-1]

    def canJump(self, nums):
        if not nums:
            return True

        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump([2,1,3,0,0,0,4]))
    print(sol.canJump([2,1,3,0,0,4]))

