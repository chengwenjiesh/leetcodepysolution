from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        cnt = Counter(changed)
        if cnt[0] % 2 == 1:
            return []

        for i in sorted(cnt):
            if cnt[2 * i] < cnt[i]:
                return []
            if i > 0:
                cnt[2 * i] -= cnt[i]
            else:
                cnt[i] //= 2

        return list(cnt.elements())

