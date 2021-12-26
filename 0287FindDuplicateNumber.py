from typing import List

class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        # O(nlogn)
        left, right = 1, len(nums) - 1
        while left < right:
            count = 0
            mid = left + (right - left) // 2
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left


    def findDuplicate(self, nums):
        # O(n)
        for i in range(len(nums)):
            if nums[abs(nums[i])] > 0:
                nums[abs(nums[i])] *= -1
            else:
                return abs(nums[i])

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([1,3,3,2,4,5]))
