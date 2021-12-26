class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff = []
        for i in range(len(nums1)):
            diff.append(nums1[i] - nums2[i])

        diff.sort()
        l, r = 0, len(diff) - 1
        result = 0

        while l < r:
            if diff[l] + diff[r] > 0:
                result += (r - l)
                r -= 1
            else:
                l += 1

        return result
