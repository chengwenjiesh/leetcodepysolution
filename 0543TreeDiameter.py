from DataStructures import TreeNode
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.findMostNodesInPath(root)[1] - 1

    def findMostNodesInPath(self, root):
        # return (longest path to leaf, max length path beneth)
        if not root:
            return (0, 0)

        ldeepest, llongest = self.findMostNodesInPath(root.left)
        rdeepest, rlongest = self.findMostNodesInPath(root.right)

        deepest = max(ldeepest, rdeepest) + 1
        longest = max(1 + ldeepest + rdeepest, llongest, rlongest)
        return (deepest, longest)


if __name__ == '__main__':
    sol = Solution()
    t3 = TreeNode(3)
    t2 = TreeNode(2, t3,None)
    t1 = TreeNode(1, t2,None)
    print(sol.diameterOfBinaryTree(t1))

