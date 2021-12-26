from DataStructures import TreeNode
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)




if __name__ == '__main__':
    sol = Solution()
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.hasPathSum(n1, 4))

