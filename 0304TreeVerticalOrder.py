from DataStructures import TreeNode
from collections import deque

class Solution:
    def verticalOrder1(self, root):
        if not root:
            return []
        leftPart = []
        rightPart = []
        # cannot guarantee for each column, numbers are from top to bottom
        self.findColumn(root, leftPart, rightPart, 0)
        return leftPart[::-1] + rightPart

    def findColumn(self, root, leftPart, rightPart, x):
        # left part: store column -10 to -1
        # right part: store column 0 to 10
        if not root:
            return

        if x < 0:
            if -x - 1 == len(leftPart):
                leftPart.append([root.val])
            else:
                leftPart[-x - 1].append(root.val)
        else:
            if x == len(rightPart):
                rightPart.append([root.val])
            else:
                rightPart[x].append(root.val)

        self.findColumn(root.left, leftPart, rightPart, x - 1)
        self.findColumn(root.right, leftPart, rightPart, x + 1)

    def verticalOrder(self, root):
        if not root:
            return []

        q = deque([(root, 0)])
        leftPart, rightPart = [], []
        while q:
            node, col = q.popleft()
            if col < 0:
                if -col - 1 == len(leftPart):
                    leftPart.append([node.val])
                else:
                    leftPart[-col - 1].append(node.val)
            else:
                if col == len(rightPart):
                    rightPart.append([node.val])
                else:
                    rightPart[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        return leftPart[::-1] + rightPart

if __name__ == '__main__':
    sol = Solution()
    t4 = TreeNode(4)
    t3 = TreeNode(3, None, t4)
    t2 = TreeNode(1, None, t3)
    t0 = TreeNode(0)
    t1 = TreeNode(2, t2, t0)
    print(sol.verticalOrder(t1))
    print(sol.verticalOrder1(t1))

