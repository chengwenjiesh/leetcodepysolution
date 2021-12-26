from DataStructures import TreeNode
from typing import List
from typing import Optional

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.findHeight(root, result)
        return result


    def findHeight(self, node, result):
        if not node:
            return -1

        height = max(self.findHeight(node.left, result), self.findHeight(node.right, result)) + 1

        if height == len(result):
            result.append([])

        result[height].append(node.val)
        return height


if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(3, n1, n2)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.findLeaves(n1))


