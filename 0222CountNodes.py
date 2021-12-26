# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        leftDepth, rightDepth = 0, 0
        l, r = root, root

        while l:
            leftDepth += 1
            l = l.left
        while r:
            rightDepth += 1
            r = r.right

        if leftDepth == rightDepth:
            return 2 ** leftDepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

