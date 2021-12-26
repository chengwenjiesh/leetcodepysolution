from DataStructures import TreeNode
from typing import List
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.findPath(root, targetSum, [], result)
        return result

    def findPath(self, node, targetSum, path, result):
        if not node:
            return

        if not node.left and not node.right:
            if targetSum == node.val:
                path.append(node.val)
                result.append(path[:])
                path.pop()
            return

        path.append(node.val)
        self.findPath(node.left, targetSum - node.val, path, result)
        self.findPath(node.right, targetSum - node.val, path, result)
        path.pop()

if __name__ == '__main__':
    sol = Solution()
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.pathSum(n1, 4))

