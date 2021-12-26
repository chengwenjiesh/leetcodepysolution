from DataStructures import TreeNode

class Solution:
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root

        newParent = self.upsideDownBinaryTree(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = root.right = None

        return newParent

if __name__ == '__main__':
    sol = Solution()
    t3 = TreeNode(3)
    t2 = TreeNode(2)
    t1 = TreeNode(1, t2, t3)
    print(sol.upsideDownBinaryTree(t1).val)

