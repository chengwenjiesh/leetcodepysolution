from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [None for _ in range(len(nums) + 1)]

        for i in cnt:
            if not buckets[cnt[i]]:
                buckets[cnt[i]] = []
            buckets[cnt[i]].append(i)

        result = []
        left = k

        while left > 0:
            for i in range(len(nums), 0, -1):
                if buckets[i]:
                    result += buckets[i]
                    left -= len(buckets[i])

        return result if len(result) == k else result[:k]



if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))

