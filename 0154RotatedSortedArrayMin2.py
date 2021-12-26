from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                # 2222212
                # 2212222
                r -= 1

        return nums[l]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([2,2,2,1,2,2,2,2,2]))
    print(sol.findMin([2,2,2,2,2,2,2,1,2]))

