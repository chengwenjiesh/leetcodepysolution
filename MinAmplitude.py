'''
Given a list of nums, return min amplitute after removing
k consecutive numbers, assume k is smaller than length of list
'''
class Solution:
    def findMinAmplitude(self, nums, k):
        # nums length is at least 2
        # k is at least 1
        # k < len(nums)
        minLeft, maxLeft = float('inf'), float('-inf')
        minRight, maxRight = float('inf'), float('-inf')
        left, right = [[minLeft, maxLeft]], [[minRight, maxRight]]

        for i in range(len(nums) - k):
            minLeft = min(minLeft, nums[i])
            maxLeft = max(maxLeft, nums[i])
            left.append([minLeft, maxLeft])

        for i in range(len(nums) - 1, k - 1, -1):
            minRight = min(minRight, nums[i])
            maxRight = max(maxRight, nums[i])
            right.append([minRight, maxRight])

        right = right[::-1]
        minAmpli = float('inf')
        print(left)
        print(right)

        for i, _ in enumerate(left):
            x = max(left[i][1], right[i][1])
            y = min(left[i][0], right[i][0])
            minAmpli = min(minAmpli, x - y)
        return minAmpli


if __name__ == '__main__':
    sol = Solution()
    nums = [3,5,1,3,9,8]
    print(sol.findMinAmplitude(nums, 4))

