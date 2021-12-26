from DataStructures import TreeNode
from typing import Optional
from typing import List
from collections import deque

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # heapq will be needed if tree is bt instead of bst
        # O(n)
        nodeQueue = deque()
        self.inorderTraverse(root, nodeQueue, target, k)
        return [x for x in nodeQueue]

    def inorderTraverse(self, root, nodeQueue, target, k):
        if not root:
            return

        self.inorderTraverse(root.left, nodeQueue, target, k)
        if len(nodeQueue) == k:
            if abs(root.val - target) < abs(nodeQueue[0] - target):
                nodeQueue.popleft()
                nodeQueue.append(root.val)
        else:
            nodeQueue.append(root.val)
        self.inorderTraverse(root.right, nodeQueue, target, k)



if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n2, n5)
    print(sol.closestKValues(n4, 2.1, 3))

