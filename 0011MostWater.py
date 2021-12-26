from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0

        while l < r:
            result = max(result, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
