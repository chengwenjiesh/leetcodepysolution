class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]


if __name__ == '__main__':
    sol = Solution()
    res = sol.singleNumber([1,2,1,3,2])
    print(res)
