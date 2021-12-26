class Solution:
    def rob(self, nums) -> int:
        # how you derive from recursion to dp
        # for each house, you either rob or skip
        rob = skip = 0
        result = 0

        for n in nums:
            rob, skip = skip + n, max(rob, skip)
            result = max(result, rob)

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([100,1,1,100]))

