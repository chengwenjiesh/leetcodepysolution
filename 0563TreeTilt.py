from DataStructure import TreeNode

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.findTiltAndSum(root)[0]

    def findTiltAndSum(self, node):
        # return all tilt sum beneath this node
        # return all node sum beneath this node
        if not node:
            return (0, 0)

        tiltL, sumL = self.findTiltAndSum(node.left)
        tiltR, sumR = self.findTiltAndSum(node.right)

        return (abs(sumL - sumR) + tiltL + tiltR, node.val + sumL + sumR)


