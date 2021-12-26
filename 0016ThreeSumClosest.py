from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # len(nums) is at least 3
        result = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                elif sum > target:
                    if sum - target < abs(result - target):
                        result = sum
                    k -= 1
                else:
                    if target - sum < abs(result - target):
                        result = sum
                    j += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClosest([1,2,0,-3],1))
