from DataStructures import TreeNode
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, root, minBound, maxBound):
        # check if all nodes under root within [minBound, maxBound]
        if not root:
            return True

        if root.val >= maxBound or root.val <= minBound:
            return False

        return self.validate(root.left, minBound, root.val) and \
               self.validate(root.right, root.val, maxBound)


if __name__ == '__main__':
    sol = Solution()
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    t2 = TreeNode(2, t1, t3)
    t4 = TreeNode(4, None, t2)
    print(sol.isValidBST(t2))
    print(sol.isValidBST(t4))
