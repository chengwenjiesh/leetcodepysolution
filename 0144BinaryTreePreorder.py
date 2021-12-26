from DataStructures import TreeNode

class Solution:
    def preorderTraversal(self, root: TreeNode):
        result = []
        self.preorderDFS(root, result)
        return result

    def preorderDFS(self, root, result):
        if root:
            result.append(root.val)
            self.preorderDFS(root.left, result)
            self.preorderDFS(root.right, result)


if __name__ == '__main__':
    sol = Solution()
    n5 = TreeNode(7)
    n4 = TreeNode(15)
    n3 = TreeNode(20, n4, n5)
    n2 = TreeNode(9)
    n1 = TreeNode(3, n2, n3)
    res = sol.preorderTraversal(n1)
    print(res)
