from DataStructures import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


if __name__ == '__main__':
    sol = Solution()
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)

