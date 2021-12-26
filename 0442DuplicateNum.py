from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
            else:
                result.append(abs(nums[i]))
        # those appear twice should be sitting on those not appearing
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicates([4,3,2,7,8,2,3,1]))

