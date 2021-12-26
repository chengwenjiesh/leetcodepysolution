from DataStructures import TreeNode
from typing import Optional
from typing import List

class Solution:
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderDFS(root, result)
        return result

    def inorderDFS(self, node, result):
        if not node:
            return

        self.inorderDFS(node.left, result)
        result.append(node.val)
        self.inorderDFS(node.right, result)

    def inorderTraversal(self, root):
        # iteratively
        result, node_stack = [], []

        while root or node_stack:
            if root:
                node_stack.append(root)
                root = root.left
            else:
                # all left subtree of last element been traversed
                root = node_stack.pop()
                result.append(root.val)
                # now traverse right subtree
                root = root.right

        return result


if __name__ == '__main__':
    sol = Solution()
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n3 = TreeNode(3, n4, n5)
    n2 = TreeNode(2)
    n1 = TreeNode(1, n2, n3)
    n6 = TreeNode(6, n1, None)
    print(sol.inorderTraversal(n1))

