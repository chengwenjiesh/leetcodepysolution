import random
import heapq

class Solution:
    def findKthLargest2(self, nums, k: int) -> int:
        # kth largest -> n - k + 1 th smallest
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

        for _ in range(len(nums) - k):
            heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

    def findKthLargest1(self, nums, k):
        max_heap = []

        for num in nums:
            heapq.heappush(max_heap, -num)

        for _ in range(k - 1):
            heapq.heappop(max_heap)

        return -heapq.heappop(max_heap)


    def findKthLargest(self, nums, k):
        # 1 <= k <= len(nums)
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, start, end, k):
        idx = self.partition(nums, start, end)
        if idx == k - 1:
            return nums[k - 1]
        elif idx > k - 1:
            return self.quickSelect(nums, start, idx - 1, k)
        else:
            return self.quickSelect(nums, idx + 1, end, k)

    def partition(self, nums, start, end):
        if start == end:
            return start

        pivotIdx = random.randint(start, end)
        pivot = nums[pivotIdx]
        nums[pivotIdx], nums[end] = nums[end], nums[pivotIdx]

        left = start
        for i in range(start, end + 1):
            if nums[i] > pivot:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

        # on the left side of idx 'left', all numbers are greater than pivot
        nums[left], nums[end] = nums[end], nums[left]
        return left


if __name__ == '__main__':
    sol = Solution()
    print([3,2,1,5,6,4,8,9,0,7])
    print(sol.findKthLargest([3,2,1,5,6,4,8,9,0,7], 4))



