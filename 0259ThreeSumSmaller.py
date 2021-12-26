from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        sz = len(nums)
        if sz < 3:
            return 0

        nums.sort()
        # lock one idx and compare the other two
        result, idx = 0, 0
        while idx < sz - 2:
            l, r = idx + 1, sz - 1
            while l < r:
                if nums[idx] + nums[l] + nums[r] < target:
                    result += (r - l)
                    l += 1
                else:
                    r -= 1
            idx += 1

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumSmaller([-1,-2,4,5,6], 8))

