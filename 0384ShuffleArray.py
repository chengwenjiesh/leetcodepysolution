from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        size = len(self.nums)
        result = self.nums[:]

        for i in range(size - 1, -1, -1):
            idx = random.randint(0, i)
            result[i], result[idx] = result[idx], result[i]

        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
