from DataStructures import TreeNode

class Solution:
    def lowestCommonAncestor(self, root, p, q) -> 'TreeNode':
        # populate p and q all the way up until they meet(if they will)
        if not root or root == p or root == q:
            return root

        leftSub = self.lowestCommonAncestor(root.left, p, q)
        rightSub = self.lowestCommonAncestor(root.right, p ,q)

        if leftSub and rightSub:
            return root

        # at least one of leftSub and rightSub is None
        return leftSub if not rightSub else rightSub




if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(3, n1, n2)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.lowestCommonAncestor(n1, n3, n4).val)

