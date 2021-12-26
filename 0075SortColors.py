class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        # number on r's right are 2
        # number on l's left are 0
        l, r = 0, len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 2 and i <= r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            while nums[i] == 0 and i >= l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1


if __name__ == '__main__':
    sol = Solution()
    a = [1,1,1,0,1,2,2,1,0]
    sol.sortColors(a)
    print(a)

