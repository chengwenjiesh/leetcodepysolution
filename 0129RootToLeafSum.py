from DataStructures import TreeNode
from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.rootSum = 0
        self.findPath(root, 0)
        return self.rootSum

    def findPath(self, root, prevSum):
        currSum = prevSum * 10 + root.val
        if not root.left and not root.right:
            self.rootSum += currSum
            return

        if root.left:
            self.findPath(root.left, currSum)
        if root.right:
            self.findPath(root.right, currSum)


if __name__ == '__main__':
    sol = Solution()
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1 = TreeNode(1, t2, t3)
    print(sol.sumNumbers(t1))

