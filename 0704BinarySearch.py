class Solution:
    def search(self, nums: [int], target: int):
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
                
        return low if nums[low] == target else -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([-1,0,3,5,9,12], 9))
    print(sol.search([-1,0,3,5,9,12], 10))
