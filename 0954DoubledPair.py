from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        if len(arr) % 2 == 1:
            return False

        cnt = Counter(arr)
        if cnt[0] % 2 == 1:
            return False

        for i in sorted(cnt, key = lambda x: abs(x)):
            if cnt[2 * i] < cnt[i]:
                return False
            if i != 0:
                cnt[2 * i] -= cnt[i]
            else:
                cnt[i] //= 2

        return True
