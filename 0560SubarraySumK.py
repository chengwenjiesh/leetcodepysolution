from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = prefixSum = 0
        prefixMap = {0:1}

        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixMap:
                result += prefixMap[prefixSum - k]
            try:
                prefixMap[prefixSum] += 1
            except KeyError as e:
                prefixMap[prefixSum] = 1

        return result

    def subarraySum1(self, nums, k):
        # works only for non-negative number
        result = l = r = 0
        chunkSum = nums[0]

        while l < len(nums) and r < len(nums):
            if chunkSum == k:
                result += 1
                if r < len(nums) - 1:
                    r += 1
                    chunkSum += nums[r]
                else:
                    l += 1
                    chunkSum -= nums[l - 1]
            elif chunkSum < k:
                if r < len(nums) - 1:
                    r += 1
                    chunkSum += nums[r]
                else:
                    break
            else:
                if l < r:
                    l += 1
                    chunkSum -= nums[l - 1]
                else:
                    if l < len(nums) - 1:
                        l, r = l + 1, r + 1
                        chunkSum = nums[l + 1]
                    else:
                        break

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraySum([1,2,3], 3))

