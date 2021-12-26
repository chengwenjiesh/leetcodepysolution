from DataStructures import TreeNode
from typing import Optional
from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBST(0, len(nums) - 1, nums)

    def buildBST(self, start, end, inorder):
        if start > end:
            return None
        if start == end:
            return TreeNode(inorder[start])

        mid = start + (end - start) // 2
        root = TreeNode(inorder[mid])
        root.left = self.buildBST(start, mid - 1, inorder)
        root.right = self.buildBST(mid + 1, end, inorder)

        return root


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedArrayToBST([1,2,3,4,5]).val)
