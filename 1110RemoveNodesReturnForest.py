from DataStructures import TreeNode

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        toDelete = set(to_delete)
        result = []
        self.removeNode(root, toDelete, result, True)
        return result

    def removeNode(self, node, toDelete, result, isRoot):
        if not node:
            return None

        nodeRemoved = node.val in toDelete
        if isRoot and not nodeRemoved:
            result.append(node)

        node.left = self.removeNode(node.left, toDelete, result, nodeRemoved)
        node.right = self.removeNode(node.right, toDelete, result, nodeRemoved)

        return node if not nodeRemoved else None

