class Solution:
    def findPermutation(self, s: str) -> List[int]:
        result = [n for n in range(1, len(s) + 2)]
        left, right = 0, 0

        while right < len(s):
            if s[right] == 'D':
                left = right
                while right < len(s) and s[right] == 'D':
                    right += 1
                # [left, right - 1] are streak of D
                self._reverse(result, left, right - 1 + 1)
            else:
                right += 1

        return result

    def _reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

