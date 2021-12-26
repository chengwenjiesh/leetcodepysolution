from DataStructures import TreeNode

class Solution:
    def countUnivalSubtrees(self, root) -> int:
        totalUni = 0

        def findUnivalSub(node):
            nonlocal totalUni
            if not node:
                return (True, None)

            isUniLeft, uniVLeft = findUnivalSub(node.left)
            isUniRight, uniVRight = findUnivalSub(node.right)

            if not isUniLeft or not isUniRight:
                return (False, node.val)

            if (uniVLeft is not None and uniVLeft != node.val) or \
               (uniVRight is not None and uniVRight != node.val):
                return (False, node.val)

            totalUni += 1
            return (True, node.val)

        findUnivalSub(root)
        return totalUni

if __name__ == '__main__':
    sol = Solution()
    t1 = TreeNode(5)
    t2 = TreeNode(5)
    t3 = TreeNode(5, t1, t2)
    t4 = TreeNode(1)
    t5 = TreeNode(3, t3, t4)
    print(sol.countUnivalSubtrees(t5))

