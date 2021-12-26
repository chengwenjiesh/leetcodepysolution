from DataStructures import TreeNode
from typing import List
from typing import Optional

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.buildBST(float('-inf'), float('inf'), preorder, 0)


    def buildBST(self, lowBound, highBound, preorder, idx):
        if idx == len(preorder):
            return None

        rootVal = preorder[idx]
        if rootVal < lowBound or rootVal > highBound:
            return None

        root = TreeNode(rootVal)
        lstart = idx + 1
        while idx < len(preorder) and preorder[idx] <= rootVal:
            idx += 1
        rstart = idx

        root.left = self.buildBST(lowBound, rootVal, preorder, lstart)
        root.right = self.buildBST(rootVal, highBound, preorder, rstart)

        return root


if __name__ == '__main__':
    sol = Solution()
    print(sol.bstFromPreorder([8,5,1,7,10,12]).val)

