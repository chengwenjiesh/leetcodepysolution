import bisect

class Solution:
    def lengthOfLIS2(self, nums:[int]) -> int:
        # O(n^2) time complexity
        lis = [1] * len(nums)
        global_lis = 1

        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    lis[i] = max(lis[j] + 1, lis[i])
                    global_lis = max(global_lis, lis[i])

        return global_lis

    def lengthOfLIS(self, nums):
        end = []
        for num in nums:
            idx = bisect.bisect_left(end, num)
            if idx == len(end):
                end.append(num)
            else:
                end[idx] = num

        return len(end)


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(sol.lengthOfLIS2([10,9,2,5,3,7,101,18]))
