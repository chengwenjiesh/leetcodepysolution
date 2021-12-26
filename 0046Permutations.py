from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.formatPermutation(nums, 0, result)
        return result

    def formatPermutation(self, nums, idx, result):
        if idx == len(nums):
            result.append(nums[:])
            return

        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.formatPermutation(nums, idx + 1, result)
            nums[idx], nums[i] = nums[i], nums[idx]


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1,2,3]))
