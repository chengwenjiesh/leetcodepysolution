from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        return [self.binarySearchLeft(nums, target), self.binarySearchRight(nums, target)]


    def binarySearchLeft(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l if nums[l] == target else -1

    def binarySearchRight(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        # consider both l and l - 1
        if nums[l] == target:
            return l
        else:
            return l - 1 if  l - 1 >= 0 and nums[l - 1] == target else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10],8))

