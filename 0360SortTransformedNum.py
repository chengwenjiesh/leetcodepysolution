from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        sz = len(nums)
        if not sz:
            return []

        trans = [a * num * num + b * num + c for num in nums]
        result = [0] * sz

        l, r = 0, sz - 1
        idx = sz - 1 if a >= 0 else 0

        while l <= r:
            if a >= 0:
                if trans[r] >= trans[l]:
                    result[idx] = trans[r]
                    r -= 1
                else:
                    result[idx] = trans[l]
                    l += 1
                idx -= 1
            else:
                if trans[r] <= trans[l]:
                    result[idx] = trans[r]
                    r -= 1
                else:
                    result[idx] = trans[l]
                    l += 1
                idx += 1

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.sortTransformedArray([-1,1,4,5], 1,2,3))

