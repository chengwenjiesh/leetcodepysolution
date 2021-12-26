from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        numStack = []
        result = []
        nums = nums + nums

        # loop twice
        for i in range(len(nums))[::-1]:
            while numStack and numStack[-1] <= nums[i]:
                numStack.pop()

            nextGreater = numStack[-1] if numStack else -1
            numStack.append(nums[i])

            if i < len(nums) // 2:
                result.append(nextGreater)

        return result[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([1,2,3,4,2]))

