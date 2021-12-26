from DataStructure import TreeNode

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l, r = self.minDepth(root.left), self.minDepth(root.right)
        if l == 0 or r == 0:
            return (l | r) + 1

        return min(l, r) + 1


