from DataStructures import TreeNode
from typing import List
from typing import Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root

if __name__ == '__main__':
    sol = Solution()
    print(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]).val)

