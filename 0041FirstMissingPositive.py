from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # min result 1
        # max result len + 1
        size = len(nums)
        for i in range(size):
            while nums[i] > 0 and nums[i] <= size and nums[i] != i + 1 \
                                                  and nums[i] != nums[nums[i] - 1]:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]

        for i in range(size):
            if nums[i] != i + 1:
                return i + 1

        return size + 1

