from DataStructures import TreeNode
from typing import Optional

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodeValues = set()

        def findNode(node):
            if not node:
                return False
            if k - node.val in nodeValues:
                return True

            nodeValues.add(node.val)

            return findNode(node.left) or findNode(node.right)

        return findNode(root)

if __name__ == '__main__':
    sol = Solution()
    t2 = TreeNode(2)
    t3 = TreeNode(4)
    t1 = TreeNode(3, t2, t3)
    print(sol.findTarget(t1, 7))
    print(sol.findTarget(t1, 10))

