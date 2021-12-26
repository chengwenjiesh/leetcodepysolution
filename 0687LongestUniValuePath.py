from DataStructures import TreeNode
from typing import Optional

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.findUniPath(root)[0] - 1

    def findUniPath(self, node):
        # return (longest unipath under node,
        #         longest top-down unipath passing node,
        #         whether whole path passing node)
        if not node:
            return (0, 0)

        lUniLen, leftPartLen = self.findUniPath(node.left)
        rUniLen, rightPartLen = self.findUniPath(node.right)

        newLeftPath = leftPartLen + 1 if node.left and node.val == node.left.val else 0
        newRightPath = rightPartLen + 1 if node.right and node.val == node.right.val else 0

        totalUniLen = max(1 + newLeftPath + newRightPath, lUniLen, rUniLen)
        return (totalUniLen, max(newLeftPath, newRightPath))



