from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) != len(nums2) or len(nums1) < 2:
            return 0
        size = len(nums1)

        # skip[i] min changes if skip this num
        # swap[i] min changes if swap this num
        skip = [0] * size
        swap = [1] * size

        for i in range(1, size):
            # in each position, array should be either self-increasing
            # or inter-increasing, or both
            slfIncr = nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]
            intIncr = nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]

            if slfIncr and intIncr:
                skip[i] = min(skip[i - 1], swap[i - 1])
                swap[i] = min(skip[i - 1], swap[i - 1]) + 1
            elif slfIncr:
                skip[i] = skip[i - 1]
                swap[i] = swap[i - 1] + 1
            elif intIncr:
                skip[i] = swap[i - 1]
                swap[i] = skip[i - 1] + 1
            else:
                return -1

        return min(skip[size - 1], swap[size - 1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.minSwap([1,3,5,4],[1,2,3,7]))

