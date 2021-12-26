class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first "non increasing"
        # find first "just larger than it" number
        # swap
        # reverse
        size = len(nums)

        right = size - 2
        while right >= 0 and nums[right] >= nums[right + 1]:
            right -= 1

        if right >= 0:
            firstLarger = size - 1
            while nums[firstLarger] <= nums[right]:
                firstLarger -= 1
            nums[right], nums[firstLarger] = nums[firstLarger], nums[right]

        start, end = right + 1, size - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return


