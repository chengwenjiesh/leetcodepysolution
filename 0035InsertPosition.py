from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        start, end = 0, len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid


        return start if nums[start] >= target else start + 1



if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1,2,5,6], 5))
    print(sol.searchInsert([1,2,5,6], 4))
    print(sol.searchInsert([1,2,5,6], -1))
    print(sol.searchInsert([1], 5))
    print(sol.searchInsert([1], -5))
    print(sol.searchInsert([], -5))
