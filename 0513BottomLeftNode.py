from DataStructures import TreeNode

class Solution:
    def findBottomLeftValue1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        curr, next = [root], []
        result = float('inf')

        while curr:
            result = curr[0].val
            for n in curr:
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            curr, next = next, []

        return result

    def findBottomLeftValue(self, root):
        if not root:
            return None

        bottom = -1
        result = root.val
        def dfs(node, lvl) -> None:
            nonlocal bottom
            nonlocal result

            if not node:
                return
            if lvl > bottom:
                bottom = lvl
                result = node.val

            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)

        dfs(root, 0)
        return result


