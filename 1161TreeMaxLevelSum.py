from DataStructures import TreeNode
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = [root]
        curr_level = 1
        max_sum_level = 1
        max_sum = root.val

        while level:
            curr_level_sum = sum([node.val for node in level])
            if curr_level_sum > max_sum:
                max_sum_level = curr_level
                max_sum = curr_level_sum

            next_level = []
            for node in level:
                next_level.extend([node.left, node.right])

            level = [node for node in next_level if node]
            curr_level += 1

        return max_sum_level



if __name__ == '__main__':
    sol = Solution()
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n4, n5)
    n2 = TreeNode(2)
    n1 = TreeNode(1, n3, n2)
    print(sol.maxLevelSum(n1))

