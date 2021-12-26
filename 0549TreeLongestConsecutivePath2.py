from DataStructures import TreeNode

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        return self.findLCP(root)[2]

    def findLCP(self, node):
        # return longest decreasing and increasing path from this node
        # maintain a global LCP as return value
        if not node:
            return (0, 0, 0)

        dwnLCPL, upLCPL, maxLCPL = self.findLCP(node.left)
        dwnLCPR, upLCPR, maxLCPR = self.findLCP(node.right)

        dwn, up, maxPath = 1, 1, 1
        if node.left:
            if node.val == node.left.val - 1:
                dwn = max(dwn, dwnLCPL + 1)
            elif node.val == node.left.val + 1:
                up = max(up, upLCPL + 1)
        if node.right:
            if node.val == node.right.val - 1:
                dwn = max(dwn, dwnLCPR + 1)
            elif node.val == node.right.val + 1:
                up = max(up, upLCPR + 1)

        maxPath = max(maxLCPL, maxLCPR, up + dwn - 1)
        return (dwn, up, maxPath)

