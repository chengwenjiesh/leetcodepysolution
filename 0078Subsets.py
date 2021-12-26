from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.formatSubset(0, result, [], nums)
        return result

    def formatSubset(self, idx, result, path, nums):
        result.append(path[:])
        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.formatSubset(i + 1, result, path, nums)
            path.pop()


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1,2,3]))

