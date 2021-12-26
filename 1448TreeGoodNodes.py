from DataStructures import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.findAllGoodNodes(root, root.val)

    def findAllGoodNodes(self, node, prevMax):
        if not node:
            return 0

        lNodes = self.findAllGoodNodes(node.left, max(prevMax, node.val))
        rNodes = self.findAllGoodNodes(node.right, max(prevMax, node.val))

        if node.val >= prevMax:
            return lNodes + rNodes + 1
        else:
            return lNodes + rNodes



