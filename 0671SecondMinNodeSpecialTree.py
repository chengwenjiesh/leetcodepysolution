from DataStructures import TreeNode
from typing import Optional

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        firstMin, secondMin = self.minValue(root)
        return -1 if secondMin == float('inf') else secondMin

    def minValue(self, node):
        # return value carries 1. smallest value 2. second smallest value
        if not node:
            return (float('inf'), float('inf'))

        lMin, lSecondMin = self.minValue(node.left)
        rMin, rSecondMin = self.minValue(node.right)
        candidate = min(i for i in[lMin, lSecondMin, rMin, rSecondMin] if i != node.val)

        return (node.val, candidate)

if __name__ == '__main__':
    sol = Solution()
    t3 = TreeNode(3)
    t2 = TreeNode(2)
    t1 = TreeNode(2, t2, t3)
    print(sol.findSecondMinimumValue(t1))


