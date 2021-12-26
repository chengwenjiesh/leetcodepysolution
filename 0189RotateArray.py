class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums is not empty
        sz = len(nums)
        k %= sz

        if k == 0:
            return

        #nums[:] = nums[sz - k :] + nums[: sz - k]
        self.reverseArray(nums, 0, sz - 1)
        self.reverseArray(nums, 0, k - 1)
        self.reverseArray(nums, k, sz - 1)

    def reverseArray(self, nums, start, end):
        l, r = start, end
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    sol = Solution()
    sol.rotate(nums, 5)
    print(nums)

