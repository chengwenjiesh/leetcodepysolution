from DataStructures import TreeNode
from typing import List

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root

        result = []
        up, down = [root], []
        while up:
            curr = []
            for node in up:
                curr.append(node.val)
                if node.left:
                    down.append(node.left)
                if node.right:
                    down.append(node.right)
            up, down = down, []
            result.append(curr)

        return result[::-1]


