from DataStructures import TreeNode
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1


    def getHeight(self, root):
        # return height if subtree is balanced
        # otherwise return -1
        if not root:
            return 0

        leftHeight, rightHeight = self.getHeight(root.left), self.getHeight(root.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1

        return max(leftHeight, rightHeight) + 1 if \
               abs(leftHeight - rightHeight) < 2 else -1



if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(3, n1, n2)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.isBalanced(n1))

