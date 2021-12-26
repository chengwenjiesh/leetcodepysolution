from typing import List

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        first = self.findFirstOccurrence(nums, target)
        checkpoint = first + len(nums) // 2
        return first <= len(nums) // 2 and checkpoint < len(nums) and nums[checkpoint] == target

    def findFirstOccurrence(self, nums, candidate):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < candidate:
                start = mid + 1
            else:
                end = mid
        return start

if __name__ == '__main__':
    sol = Solution()
    print(sol.isMajorityElement([1,2,101,101], 101))
    print(sol.isMajorityElement([1,2,101,101,101], 101))
