from DataStructures import TreeNode
from collections import deque
from typing import List

class Solution:
    def rightSideView(self, root):
        return self.rightSideViewBFS(root)

    def rightSideViewBFS(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        curr, nxt = [root], []
        while curr:
            result.append(curr[0].val)
            for n in curr:
                if n.right:
                    nxt.append(n.right)
                if n.left:
                    nxt.append(n.left)
            curr, nxt = nxt, []

        return result

    def rightSideViewDFS(self, root):
        result = []
        self.rightSideViewPerLevel(root, result, 0)
        return result

    def rightSideViewPerLevel(self, root, result, depth):
        if not root:
            return
        if depth == len(result):
            result.append(root.val)

        self.rightSideViewPerLevel(root.right, result, depth + 1)
        self.rightSideViewPerLevel(root.left, result, depth + 1)


if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(3, n1, n2)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.rightSideViewBFS(n1))
    print(sol.rightSideViewDFS(n1))

