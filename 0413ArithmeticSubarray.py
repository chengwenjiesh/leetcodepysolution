from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        arith_end_idx = [0] * len(nums)
        total_cnt = 0

        for i in range(2, len(nums)):
            # i - 2, i - 1, i can form array
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                arith_end_idx[i] = 1 + arith_end_idx[i - 1]
                total_cnt += arith_end_idx[i]

        return total_cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArithmeticSlices([1,2,3,4]))

