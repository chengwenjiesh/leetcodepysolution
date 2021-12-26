from DataStructures import TreeNode
from typing import Optional
from typing import List

class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        # recursion
        if not root:
            return [None, None]

        if target == root.val:
            newRight = root.right
            root.right = None
            return [root, newRight]

        elif target > root.val:
            newLeft, newRight = self.splitBST(root.right, target)
            root.right = newLeft
            return [root, newRight]

        elif target < root.val:
            newLeft, newRight = self.splitBST(root.left, target)
            root.left = newRight
            return [newLeft, root]



if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(3)
    n3 = TreeNode(2, n1, n2)
    n4 = TreeNode(5)
    n1 = TreeNode(4, n3, n4)
    ans = sol.splitBST(n1, 3)
    print(ans[0].val, ans[1].val)

