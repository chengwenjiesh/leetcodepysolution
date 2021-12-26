from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force -> O(n^3)
        # sort + two pointers -> O(n^2)
        if len(nums) < 3:
            return []

        result = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    # avoid adding duplicate result
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,4]))

