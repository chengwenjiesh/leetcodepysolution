from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums


    def mergeSort(self, nums):
        if len(nums) < 2:
            return

        mid = (len(nums) - 1) // 2
        left, right = nums[:mid + 1], nums[mid + 1:]
        self.mergeSort(left)
        self.mergeSort(right)
        pt1, pt2, pt = 0, 0, 0

        while pt1 < len(left) and pt2 < len(right):
            if left[pt1] <= right[pt2]:
                nums[pt] = left[pt1]
                pt1 += 1
            else:
                nums[pt] = right[pt2]
                pt2 += 1
            pt += 1

        while pt1 < len(left):
            nums[pt] = left[pt1]
            pt1 += 1
            pt += 1
        while pt2 < len(right):
            nums[pt] = right[pt2]
            pt2 += 1
            pt += 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArray([3,4,5,1,6,2,9,7]))

