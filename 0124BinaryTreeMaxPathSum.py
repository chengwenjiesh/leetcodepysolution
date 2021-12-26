from DataStructures import TreeNode
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.findMaxPath(root)[1]


    def findMaxPath(self, node):
        if not node:
            return (0, float('-inf'))

        leftSum, lmax = self.findMaxPath(node.left)
        rightSum, rmax = self.findMaxPath(node.right)

        leftSum = max(0, leftSum)
        rightSum = max(0, rightSum)

        nmax = max(node.val + leftSum + rightSum, lmax, rmax)
        return (node.val + max(leftSum, rightSum), nmax)


if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(15)
    n2 = TreeNode(3)
    n3 = TreeNode(20, n1, n2)
    n4 = TreeNode(5)
    n1 = TreeNode(-10, n3, n4)
    print(sol.maxPathSum(n1))

