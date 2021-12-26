import heapq

class Solution():
    def sortNearlySorted(self, nums, k):
        # use insertion sort
        # O(nk)
        for idx in range(1, len(nums)):
            prev, num = idx - 1, nums[idx]

            while prev >= 0 and nums[prev] > num:
                nums[prev + 1] = nums[prev]
                prev -= 1

            nums[prev + 1] = num

        return

    def sortNearlySorted2(self, nums, k):
        n = len(nums)
        heapSize = k + 1 if k < n else n
        minHeap = []

        # O(k)
        for i in range(heapSize):
            heapq.heappush(minHeap, nums[i])

        # O((n - k)*logk)
        idx = 0
        for i in range(k + 1, n):
            nums[idx] = heapq.heappop(minHeap)
            idx += 1
            heapq.heappush(minHeap, nums[i])

        # O(logk)
        while minHeap:
            nums[idx] = heapq.heappop(minHeap)
            idx += 1

        return


if __name__ == '__main__':
    sampleA = [6, 5, 3, 2, 8, 10, 9]
    sampleB = [10, 9, 8, 7, 4, 70, 60, 50]

    sol = Solution()
    sol.sortNearlySorted2(sampleA, 3)
    sol.sortNearlySorted2(sampleB, 4)

    print(sampleA)
    print(sampleB)
