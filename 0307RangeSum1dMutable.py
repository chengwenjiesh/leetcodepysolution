from typing import List

class NumArray1:

    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.nums = nums
        self.bits = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.buildBIT(i + 1, num)


    def buildBIT(self, idx, num):
        while idx <= self.length:
            self.bits[idx] += num
            lowbit = idx & (-idx)
            idx += lowbit


    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.buildBIT(index + 1, diff)

    def prefixSum(self, index):
        result = 0
        index += 1
        while index > 0:
            result += self.bits[index]
            lowbit = index & (-index)
            index -= lowbit
        return result


    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right) - self.prefixSum(left - 1)

class SegmentTreeNode:
    def __init__(self, val, start, end, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right
 
class NumArray:
    def __init__(self, nums):
        if not nums:
            self.root = None
        else:
            self.root = self._buildTree(nums, 0, len(nums) - 1)
        self.nums = nums

    def _buildTree(self, nums, start, end):
        if start == end:
            return SegmentTreeNode(nums[start], start, end)

        mid = start + (end - start) // 2
        left = self._buildTree(nums, start, mid)
        right = self._buildTree(nums, mid + 1, end)
        return SegmentTreeNode(left.val + right.val, start, end, left, right)

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val

        self.root.val += diff
        curr = self.root
        while curr.left:
            if index <= curr.left.end:
                curr.left.val += diff
                curr = curr.left
            else:
                curr.right.val += diff
                curr = curr.right

    def _queryTree(self, node, start, end):
        l, r = node.start, node.end
        if start <= l and end >= r:
            return node.val

        mid = l + (r - l) // 2
        if start > mid:
            return self._queryTree(node.right, start, end)
        elif end <= mid:
            return self._queryTree(node.left, start, end)
        else:
            return self._queryTree(node.left, start, end) + \
                   self._queryTree(node.right, start, end)

    def sumRange(self, left, right):
        return self._queryTree(self.root, left, right)


if __name__ == '__main__':
    sol = NumArray([1,2,3,4,5])
    sol.update(0,10)
    print(sol.sumRange(0,1))
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
