from DataStructures import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return subRoot is None

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)


    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        return t1.val == t2.val and self.isSameTree(t1.left, t2.left) \
                                and self.isSameTree(t1.right, t2.right)


