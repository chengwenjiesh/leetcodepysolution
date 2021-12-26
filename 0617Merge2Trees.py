from DataStructures import TreeNode

class Solution:
    def mergeTrees(self, root1, root2):
        if not root1 or not root2:
            return root1 or root2

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

if __name__ == '__main__':
    sol = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    print(sol.mergeTrees(t1,t2).val)

