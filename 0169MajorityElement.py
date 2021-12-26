from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, None
        
        for num in nums:
            if not count:
                count += 1
                candidate = num
            else:
                count += (1 if num == candidate else -1)
        
        return candidate


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([1,1,2,2,1,3,4,1,1,1]))
