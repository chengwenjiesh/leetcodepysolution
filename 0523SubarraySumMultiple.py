class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        # k > 0
        sumMap = {0:-1}
        prefixSum = 0

        for idx, n in enumerate(nums):
            prefixSum += n
            prefixSum %= k

            if prefixSum in sumMap:
                if sumMap[prefixSum] < idx - 1:
                    return True
            else:
                sumMap[prefixSum] = idx

        return False


if __name__ == '__main__':
    sol = Solution()
    print("[1,0,0]" + str(sol.checkSubarraySum([1,0,0], 5)))
    print("[1,0,1]" + str(sol.checkSubarraySum([1,0,1], 5)))
    print("[1,0,6]" + str(sol.checkSubarraySum([1,0,6], 6)))

