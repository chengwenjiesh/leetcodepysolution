from DataStructures import TreeNode
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                break
            q.append(node.left)
            q.append(node.right)

        return not any(q)


if __name__ == '__main__':
    sol = Solution()
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t2 = TreeNode(2, t4, t5)
    t6 = TreeNode(6)
    t3 = TreeNode(3, t6, None)
    t1 = TreeNode(1, t2, t3)
    print(sol.isCompleteTree(t1))

