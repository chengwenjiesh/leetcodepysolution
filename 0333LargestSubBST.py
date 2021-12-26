from DataStructures import TreeNode

class Solution:
    def largestBSTSubtree(self, root) -> int:
        if not root:
            return 0
        result = 1

        def findLargest(node):
            nonlocal result
            if not node:
                return (0, float('inf'), float('-inf'))

            # what we need to update in this level
            # what we need to pass to upper level
            lCnt, lMin, lMax = findLargest(node.left)
            rCnt, rMin, rMax = findLargest(node.right)

            if lCnt == -1 or rCnt == -1 or node.val <= lMax or node.val >= rMin:
                return (-1, 0, 0)

            currCnt = lCnt + rCnt + 1
            result = max(result, currCnt)

            return (currCnt, min(lMin, node.val), max(rMax, node.val))

        findLargest(root)
        return result

if __name__ == '__main__':
    sol = Solution()
    t4 = TreeNode(4)
    t3 = TreeNode(3, None, t4)
    t2 = TreeNode(2, None, t3)
    t1 = TreeNode(1, t2, None)
    print(sol.largestBSTSubtree(t1))


