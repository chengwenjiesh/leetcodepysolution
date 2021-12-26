from DataStructures import TreeNode
from typing import Optional

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # starting from root, using binary search to note each node val
        # constantly check if curr node is closer than target than predecessor
        # assumption: tree is not None
        result = root.val
        diff = abs(root.val - target)
        while root:
            root = root.left if root.val > target else root.right
            if root:
                if abs(root.val - target) < diff:
                    result = root.val
                    diff = abs(root.val - target)

        return result

if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n2, n5)
    print(sol.closestValue(n4, 2.1))

