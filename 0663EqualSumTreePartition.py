from DataStructures import TreeNode
from typing import Optional


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        treeSum = set()

        def getSum(node):
            if not node:
                return 0

            nodeSum = node.val + getSum(node.left) + getSum(node.right)
            if node is not root:
                treeSum.add(nodeSum)
            return nodeSum

        return getSum(root) / 2 in treeSum


if __name__ == '__main__':
    sol = Solution()
    t2 = TreeNode(1)
    t3 = TreeNode(2)
    t1 = TreeNode(0, t3, t2)
    print(sol.checkEqualTree(t1))

