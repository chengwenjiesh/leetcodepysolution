class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        result = float('inf')
        for i in range(4):
            result = min(result, nums[len(nums) - 4 + i] - nums[i])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDifference([6,6,0,1,1,4,6]))
    print(sol.minDifference([82,81,95,75,20]))

