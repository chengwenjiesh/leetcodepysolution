class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        firstSum, secondSum = {}, {}
        size = len(nums1)
        for i in range(size):
            for j in range(size):
                numSum = nums1[i] + nums2[j]
                if numSum in firstSum:
                    firstSum[numSum].append((i, j))
                else:
                    firstSum[numSum] = [(i, j)]

        result = 0
        for i in range(size):
            for j in range(size):
                numSum = nums3[i] + nums4[j]
                if -numSum in firstSum:
                    result += len(firstSum[-numSum])

        return result

