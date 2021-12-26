class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        result = float('inf')
        start = end = 0
        chunkSum = 0

        while end < len(nums):
            chunkSum += nums[end]
            end += 1

            while chunkSum >= target:
                result = min(result, end - start)
                chunkSum -= nums[start]
                start += 1

        return 0 if result == float('inf') else result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(5,[1,1,1,1]))
    print(sol.minSubArrayLen(8,[1,2,3,4]))

