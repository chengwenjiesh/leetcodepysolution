class Solution:
    def minMoves(self, nums) -> int:
        # increase (n - 1) is equivelant to decrease 1
        sumNum, minNum = nums[0], nums[0]
        for i in range(1, len(nums)):
            sumNum += nums[i]
            minNum = min(minNum, nums[i])

        return sumNum - minNum * len(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.minMoves([1,2,6]))

