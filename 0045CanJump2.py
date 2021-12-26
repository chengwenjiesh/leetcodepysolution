from typing import List

class Solution:
    def jumpDP(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        steps = [float('inf')] * len(nums)
        steps[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            prevMin = float('inf')
            for j in range(nums[i]):
                prevMin = min(prevMin, steps[min(len(nums) - 1, i + j + 1)])
                steps[i] = prevMin + 1

        return steps[0]

    def jump(self, nums):
        if len(nums) < 2:
            return 0

        count = prev = curr = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return count

            curr = max(curr, i + nums[i])
            if i == prev:
                count += 1
                prev = curr

        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.jump([2,3,5,1,4]))

