from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        size = len(arr)
        if size < 2:
            return size

        seen = {}
        result = 1
        for num in arr:
            if num not in seen:
                seen[num] = 1
            if num - difference in seen:
                seen[num] = max(seen[num - difference] + 1, seen[num])
                result = max(result, seen[num])

        return result if difference else result - 1


