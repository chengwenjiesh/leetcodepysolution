from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2, idx = m - 1, n - 1, m + n - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            idx -= 1

        if idx1 < 0:
            # append all nums2 remaining
            while idx2 >= 0:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
                idx -= 1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [3,6,9,12,16,0,0,0,0,0,0,0]
    nums2 = [2,7,8,11,14,17,18]
    sol.merge(nums1, 5, nums2, 7)
    print(nums1)
