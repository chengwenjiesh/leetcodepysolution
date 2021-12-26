from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for i in range(1, len(nums)):
            result.append(result[-1] * nums[i - 1])

        prev = 1
        for i in range(len(nums) - 2, -1, -1):
            prev = nums[i + 1] * prev
            result[i] *= prev

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))

