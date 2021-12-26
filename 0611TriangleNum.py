from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz < 3:
            return 0

        result, idx = 0, sz - 1
        nums.sort()

        while idx >= 2:
            l, r = 0, idx - 1
            while l < r:
                if nums[l] + nums[r] > nums[idx]:
                    result += (r - l)
                    r -= 1
                else:
                    l += 1
            idx -= 1

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.triangleNumber([2,2,3,4]))

