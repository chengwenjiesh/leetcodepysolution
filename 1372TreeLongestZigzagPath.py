from DataStructures import TreeNode

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.findZigZag(root)[2] - 1

    def findZigZag(self, root) -> tuple[int]:
        '''
        longest path if root is treated as left child
        longest path if root is treated as right child
        global max len
        '''
        if not root:
            return (0, 0, 0)

        left, right = self.findZigZag(root.left), self.findZigZag(root.right)
        curLeft = right[1] + 1
        curRight = left[0] + 1
        maxLen = max(curLeft, curRight, left[2], right[2])
        return (curLeft, curRight, maxLen)


