from DataStructures import TreeNode

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        lca, cnt = self.findLCA(root, p, q)
        return lca if cnt == 2 else None

    def findLCA(self, root, p, q):
        if not root:
            return (root, 0)

        leftLCA, lCnt = self.findLCA(root.left, p, q)
        rightLCA, rCnt = self.findLCA(root.right, p, q)

        pqCnt = lCnt + rCnt
        if root == p or root == q:
            return (root, pqCnt + 1)

        if leftLCA and rightLCA:
            return (root, pqCnt)

        return (leftLCA, pqCnt) if leftLCA else (rightLCA, pqCnt)


if __name__ == '__main__':
    sol = Solution()
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.lowestCommonAncestor(n1, n3, n4).val)

