from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currLen, maxLen = 0, 0
        l, r = 0, 0
        hasZero = 0

        while r < len(nums):
            if nums[r] == 1 or (nums[r] == 0 and hasZero == 0):
                if nums[r] == 0:
                    hasZero = 1
                currLen = r - l + 1
                maxLen = max(currLen, maxLen)
                r += 1
            else:
                hasZero = 0 if nums[l] == 0 else 1
                l += 1

        return maxLen


