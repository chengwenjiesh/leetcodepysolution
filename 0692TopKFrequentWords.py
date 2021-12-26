from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        buckets = [None for _ in range(len(words) + 1)]

        for w in cnt:
            freq = cnt[w]
            if not buckets[freq]:
                buckets[freq] = [w]
            else:
                buckets[freq].append(w)

        result = []
        left = k
        while left > 0:
            for i in range(len(buckets) - 1, 0, -1):
                if buckets[i]:
                    heapq.heapify(buckets[i])
                    while left > 0 and buckets[i]:
                        result.append(heapq.heappop(buckets[i]))
                        left -= 1

        return result if len(result) == k else result[:k]



if __name__ == '__main__':
    sol = Solution()
    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    print(sol.topKFrequent(words, 4))

