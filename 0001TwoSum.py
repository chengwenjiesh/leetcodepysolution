class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        target_remain = {}
        result = []
        
        for idx, num in enumerate(nums):
            if num in target_remain:
                result.append(target_remain[num])
                result.append(idx)
            else:
                target_remain[target - num] = idx
                
        return result


if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum([2, 7, 11, 15], 9)
    print(res)
