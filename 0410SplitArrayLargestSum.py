from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = -1, 0
        for num in nums:
            low = max(low, num)
            high += num

        while low < high:
            mid = low + (high - low) // 2
            if self.canSplit(nums, m, mid):
                high = mid
            else:
                low = mid + 1

        return low

    def canSplit(self, nums, m, upperBound):
        subSum, subCnt = 0, 1

        for num in nums:
            subSum += num
            if subSum > upperBound:
                subSum = num
                subCnt += 1
                if subCnt > m:
                    return False

        return True



