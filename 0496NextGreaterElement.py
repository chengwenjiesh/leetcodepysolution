from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numStack = []
        numMap = {}

        for i in range(len(nums2) - 1, -1, -1):
            while numStack and numStack[-1] <= nums2[i]:
                numStack.pop()

            nextGreaterIdx = numStack[-1] if numStack else -1
            numMap[nums2[i]] = nextGreaterIdx
            numStack.append(nums2[i])

        result = []
        for num in nums1:
            result.append(numMap[num])

        return result


if __name__ =='__main__':
    sol = Solution()
    print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))

