class Solution:
    def largestSubarray(self, nums, k):
        maxValue = max(nums[:len(nums) - k + 1])
        maxIdx = nums.index(maxValue)
        return nums[maxIdx:maxIdx + k]

    def largestSubarray2(self, nums, k):
        # what if there can be deplicate in nums?
        pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestSubarray([1,2,5,4,6], 3))
