from DataStructures import TreeNode
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSymmetricSubtree(root.left, root.right)

    def isSymmetricSubtree(self, p, q):
        if not p or not q:
            return p == q

        return p.val == q.val and self.isSymmetricSubtree(p.left, q.right) \
                              and self.isSymmetricSubtree(p.right, q.left)




if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(3)
    n3 = TreeNode(2, n1, n2)
    n4 = TreeNode(5)
    n1 = TreeNode(4, n3, n4)
    print(sol.isSymmetric(n1))

