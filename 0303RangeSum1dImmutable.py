class NumArray:

    def __init__(self, nums):
        self.numSum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            self.numSum[i] = self.numSum[i - 1] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.numSum[right]
        else:
            return self.numSum[right] - self.numSum[left - 1]



if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))
