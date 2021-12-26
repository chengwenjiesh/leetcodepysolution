from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)

        result = 0
        for i in range(size // 2):
            result = max(result, nums[i] + nums[size - 1 - i])
        return result

