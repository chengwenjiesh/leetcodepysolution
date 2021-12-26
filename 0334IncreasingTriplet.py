from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = medium = float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= medium:
                medium = num
            else:
                return True

        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.increasingTriplet([1,1,1,1,1,1]))

