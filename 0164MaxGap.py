from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        minNum, maxNum = min(nums), max(nums)
        gap = 0 - (minNum - maxNum) // (len(nums) - 1)
        
        if not gap:
            return gap
        
        bucketMin,bucketMax = [float('inf')] * (len(nums)), [float('-inf')] * (len(nums))
        for num in nums:
            idx = (num - minNum) // gap
            bucketMin[idx] = min(bucketMin[idx], num)
            bucketMax[idx] = max(bucketMax[idx], num)
        
        # scan each bucket, max gap should be in between two buckets
        maxGap = 0
        prevMax = float('-inf')
        for i in range(len(nums)):
            if bucketMin[i] == float('inf'):
                # empty bucket
                continue
            else:
                if prevMax != float('-inf'):
                    maxGap = max(maxGap, bucketMin[i] - prevMax)
                prevMax = bucketMax[i]
                    
        return maxGap


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumGap([3,6,9,1]))
