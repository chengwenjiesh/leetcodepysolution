from DataStructures import TreeNode
from typing import List

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root

        result = []
        up, down = [root], []
        level = 0
        while up:
            curr = []
            for node in up:
                curr.append(node.val)
                if node.left:
                    down.append(node.left)
                if node.right:
                    down.append(node.right)
            up, down = down, []
            if level:
                result.append(curr[::-1])
            else:
                result.append(curr)
            level = 1 - level

        return result


if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(3)
    n3 = TreeNode(2, n1, n2)
    n4 = TreeNode(5)
    n1 = TreeNode(4, n3, n4)
    print(sol.zigzagLevelOrder(n1))

