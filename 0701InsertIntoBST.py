from DataStructures import TreeNode
from typing import Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(3)
    n3 = TreeNode(2, n1, n2)
    n4 = TreeNode(5)
    n1 = TreeNode(4, n3, n4)
    ans = sol.insertIntoBST(n1, 3)
    print(ans)
