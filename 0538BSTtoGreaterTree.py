from DataStructures import TreeNode

class Solution:
    def convertBST(self, root):
        self.reverseInorder(root, 0)
        return root

    def reverseInorder(self, root: TreeNode, val: int) -> int:
        if not root:
            return val

        rightSum = self.reverseInorder(root.right, val)
        root.val += rightSum
        leftSum = self.reverseInorder(root.left, root.val)

        return leftSum


if __name__ == '__main__':
    sol = Solution()
    n0 = TreeNode(10)
    n1 = TreeNode(8)
    n2 = TreeNode(9, n1, n0)
    n3 = TreeNode(5, None, n2)
    print(sol.convertBST(n3).val)

