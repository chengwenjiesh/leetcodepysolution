from DataStructures import TreeNode
from typing import Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            newRightChild = self.deleteNode(root.right, key)
            root.right = newRightChild

        elif key < root.val:
            newLeftChild = self.deleteNode(root.left, key)
            root.left = newLeftChild

        elif key == root.val:
            # determine whether we can directly remove
            # or structure a new tree
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            smallest = self.findSmallest(root.right)
            smallest.left = root.left
            root = root.right

        return root

    def findSmallest(self, node):
        # find smallest node in tree
        if not node:
            return None

        while node.left:
            node = node.left

        return node



if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(3, n1, n2)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.deleteNode(n1, 1))

