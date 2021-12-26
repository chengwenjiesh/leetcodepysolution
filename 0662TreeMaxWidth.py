from DataStructure import TreeNode

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 1
        curr, nxt = [(root, 0)], []

        while curr:
            result = max(result, curr[-1][1] - curr[0][1] + 1)
            for node, position in curr:
                if node.left:
                    nxt.append((node.left, position * 2))
                if node.right:
                    nxt.append((node.right, position * 2 + 1))

            curr, nxt = nxt, []

        return result

