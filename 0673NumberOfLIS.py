from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # lcs: len of lcs
        # cnt: cnt of lcs
        lcs = [1] * len(nums)
        cnt = [1] * len(nums)
        global_lcs = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lcs[j] + 1 > lcs[i]:
                        lcs[i] = lcs[j] + 1
                        cnt[i] = cnt[j]
                    elif lcs[j] + 1 == lcs[i]:
                        cnt[i] += cnt[j]
            global_lcs = max(global_lcs, lcs[i])

        result = 0
        for i in range(len(nums)):
            if lcs[i] == global_lcs:
                result += cnt[i]
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.findNumberOfLIS([1,3,5,4,7]))
    print(sol.findNumberOfLIS([1,1,1,1,1,1]))
