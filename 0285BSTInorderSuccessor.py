from DataStructures import TreeNode
from typing import Optional

class Solution:
    def inorderSuccessor1(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            leftSub = self.inorderSuccessor(root.left, p)
            return leftSub if leftSub else root

    def inorderSuccessor(self, root, p):
        suc = None
        while root:
            if p.val < root.val:
                suc = root
                root = root.left
            else:
                root = root.right

        return suc


if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n2, n5)
    print(sol.inorderSuccessor(n4, n1).val)
    print(sol.inorderSuccessor1(n4, n1).val)

