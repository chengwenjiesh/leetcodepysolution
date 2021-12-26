from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        if not sz:
            return []

        result = [0] * sz
        idx = sz - 1
        l, r = 0, sz - 1

        while l <= r:
            if nums[l] ** 2 >= nums[r] ** 2:
                result[idx] = nums[l] ** 2
                l += 1
            else:
                result[idx] = nums[r] ** 2
                r -= 1
            idx -= 1

        return result


