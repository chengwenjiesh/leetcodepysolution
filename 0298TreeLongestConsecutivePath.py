from DataStructures import TreeNode
from typing import Optional

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        return self.findSequence(root)[1]


    def findSequence(self, root):
        if not root:
            return (0, 0)

        lseq, lmax = self.findSequence(root.left)
        rseq, rmax = self.findSequence(root.right)

        currLen = 1
        if lseq > 0 and root.val + 1 == root.left.val:
            currLen = max(currLen, 1 + lseq)
        if rseq > 0 and root.val + 1 == root.right.val:
            currLen = max(currLen, 1 + rseq)

        return (currLen, max(currLen, lmax, rmax))



if __name__ == '__main__':
    sol = Solution()
    n5 = TreeNode(5)
    n3 = TreeNode(3, n5, None)
    n2 = TreeNode(2, n3, None)
    n1 = TreeNode(1, None, n2)
    print(sol.longestConsecutive(n1))

