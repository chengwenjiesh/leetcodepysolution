class Solution:
    def maxProduct(self, nums):
        maxProd = minProd = result = nums[0]

        for i in range(1, len(nums)):
            maxProd = max(maxProd * nums[i], minProd * nums[i], nums[i])
            minProd = min(maxProd * nums[i], minProd * nums[i], nums[i])
            result = max(result, maxProd)

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))
