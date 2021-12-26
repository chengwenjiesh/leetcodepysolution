from typing import List

class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz < 2:
            return sz

        lcs = {}
        for num in nums:
            lcs[num] = 0
        result = 1

        def findLCS(num):
            nonlocal result
            if lcs[num] > 0:
                return lcs[num]

            if num + 1 in lcs:
                lcs[num] = 1 + findLCS(num + 1)
                result = max(result, lcs[num])
            else:
                lcs[num] = 1

            return lcs[num]

        for num in nums:
            findLCS(num)

        return result

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0

        for num in numSet:
            if num - 1 not in numSet:
                next = num + 1
                while next in numSet:
                    next += 1
                best = max(best, next - num)

        return best

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([4,1,3,2,6]))

