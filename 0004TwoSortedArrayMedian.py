class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA, lenB = len(nums1), len(nums2)
        k1, k2 = (lenA + lenB + 1) // 2, (lenA + lenB + 2) // 2
        return (self.findKthSmallest(nums1, 0, nums2, 0, k1) + \
                self.findKthSmallest(nums1, 0, nums2, 0, k2)) / 2.0

    def findKthSmallest(self, nums1, start1, nums2, start2, k):
        if start1 >= len(nums1):
            return nums2[start2 + k - 1]
        if start2 >= len(nums2):
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        mid1 = start1 + k // 2 - 1
        mid2 = start2 + k // 2 - 1
        val1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
        val2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

        if val1 >= val2:
            return self.findKthSmallest(nums1, start1, nums2, mid2 + 1, k - k // 2)
        else:
            return self.findKthSmallest(nums1, mid1 + 1, nums2, start2, k - k // 2)

