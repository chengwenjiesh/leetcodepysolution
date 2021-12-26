from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1 <= k <= len(nums)
        result = []
        candidates = deque()   #(idx, num)
        for i in range(len(nums)):
            while candidates and candidates[-1][1] <= nums[i]:
                candidates.pop()
            if candidates and candidates[0][0] < i - k + 1:
                candidates.popleft()
            candidates.append((i, nums[i]))
            
            if i >= k - 1:
                result.append(candidates[0][1])
            
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

