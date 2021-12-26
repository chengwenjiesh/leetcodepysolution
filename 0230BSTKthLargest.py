from DataStructures import TreeNode
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.result = None

        self.findNode(root)
        return self.result

    def findNode(self, root):
        if root.left:
            self.findNode(root.left)

        self.count -= 1
        if self.count == 0:
            self.result = root.val
            return

        if root.right:
            self.findNode(root.right)



if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(3)
    n3 = TreeNode(2, n1, n2)
    n4 = TreeNode(5)
    n1 = TreeNode(4, n3, n4)
    print(sol.kthSmallest(n1, 3))
