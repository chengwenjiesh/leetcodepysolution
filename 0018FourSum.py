from typing import List

class Solution:
    def fourSumAnyQuadruplet(self, nums: List[int], target: int) -> List[List[int]]:
        sz = len(nums)
        if sz < 4:
            return []

        pair = []
        nums.sort()
        for i in range(sz):
            for j in range(i + 1, sz):
                pair.append((nums[i] + nums[j], i, j))

        pair.sort(key=lambda x: (x[0], x[1], x[2]))
        l, r = 0, len(pair) - 1
        while l < r:
            if pair[l][0] + pair[r][0] == target:
                i, j, k, l = pair[l][1], pair[l][2], pair[r][1], pair[r][2]
                if i ^ j ^ k ^ l != 0:
                    return [nums[i], nums[j], nums[k], nums[l]]
            elif pair[l][0] + pair[r][0] > target:
                r -= 1
            else:
                l += 1
        return []

    def fourSum1(self, nums, target):
        sz = len(nums)
        if sz < 4:
            return []

        result = []
        nums.sort()
        for i in range(sz):
            for j in range(i + 1, sz):
                remain = target - nums[i] - nums[j]
                k, l = j + 1, sz - 1
                while k < l:
                    if nums[k] + nums[l] == remain:
                        result.append((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif nums[k] + nums[l] > remain:
                        l -= 1
                    else:
                        k += 1
        return set(result)

    def fourSum(self, nums, target):
        sz = len(nums)
        if sz < 4:
            return []

        result = []
        nums.sort()
        i = 0
        while i < sz:
            j = i + 1
            while j < sz:
                remain = target - nums[i] - nums[j]
                k, l = j + 1, sz - 1
                while k < l:
                    if nums[k] + nums[l] == remain:
                        print((i,j,k,l))
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif nums[k] + nums[l] > remain:
                        l -= 1
                    else:
                        k += 1

                while j + 1 < sz and nums[j] == nums[j + 1]:
                    j += 1
                j += 1

            while i + 1 < sz and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum([2,2,2,2,2], 8))

