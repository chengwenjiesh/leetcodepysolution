from DataStructures import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        return self.findLCA(root, set(nodes))

    def findLCA(self, root, nodeSet):
        if not root or root in nodeSet:
            return root

        leftSub = self.findLCA(root.left, nodeSet)
        rightSub = self.findLCA(root.right, nodeSet)

        if leftSub and rightSub:
            return root

        return leftSub if leftSub else rightSub


if __name__ == '__main__':
    sol = Solution()
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n4, n5)
    n2 = TreeNode(2)
    n1 = TreeNode(1, n3, n2)
    print(sol.lowestCommonAncestor(n1, [n2, n3,n5]).val)

