class Solution:
    def rob(self, nums) -> int:
        return max(self.robLine(nums[:-1]), self.robLine(nums[1:])) if len(nums) > 1 else nums[0]

    def robLine(self, nums):
        rob = skip = 0
        result = 0

        for n in nums:
            rob, skip = skip + n, max(rob, skip)
            result = max(result, rob)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([2,3,2]))

