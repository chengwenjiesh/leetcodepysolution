from DataStructures import TreeNode

class Solution:
    def rob(self, root) -> int:
        result = self.robWays(root)
        return max(result[0], result[1])

    def robWays(self, node):
        #(max money robbing this node, max money not robbing this mode)
        if not node:
            return (0, 0)

        lMoney = self.robWays(node.left)
        rMoney = self.robWays(node.right)

        # rob this node
        execute = node.val + lMoney[1] + rMoney[1]
        skip = max(lMoney[0], lMoney[1]) + max(rMoney[0], rMoney[1])

        return (execute, skip)

if __name__ == '__main__':
    sol = Solution()
    t1 = TreeNode(105)
    t2 = TreeNode(1, t1, None)
    t3 = TreeNode(100)
    t4 = TreeNode(1, t3, t2)
    print(sol.rob(t4))

