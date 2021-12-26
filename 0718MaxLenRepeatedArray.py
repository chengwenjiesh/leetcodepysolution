from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        sz1, sz2 = len(nums1), len(nums2)
        dp = [[0] * sz2 for _ in range(sz1)]
        maxLen = 0

        for i in range(sz1):
            for j in range(sz2):
                if nums1[i] == nums2[j]:
                    if not i or not j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    maxLen = max(maxLen, dp[i][j])

        return maxLen

if __name__ == '__main__':
    sol = Solution()
    print(sol.findLength([1,2,3,2,1], [3,2,1,4,7]))

