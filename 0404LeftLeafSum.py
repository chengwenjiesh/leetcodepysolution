from DataStructures import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.findLeftLeaf(root.left, 0) + self.findLeftLeaf(root.right, 1)

    def findLeftLeaf(self, node, flag):
            # flag is 0 -> left child of parent
            #.        1 -> right
        if not node:
            return 0
        if not node.left and not node.right:
            return node.val if not flag else 0

        return self.findLeftLeaf(node.left, 0) + self.findLeftLeaf(node.right, 1)

