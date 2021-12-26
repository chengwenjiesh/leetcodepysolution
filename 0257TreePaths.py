from DataStructures import TreeNode

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []

        result = []
        self.findPaths(root, "", result)
        return result

    def findPaths(self, node, curr, result):
        if node:
            if not node.left and not node.right:
                curr = curr + str(node.val)
                result.append(curr)

            self.findPaths(node.left, curr + str(node.val) + "->", result)
            self.findPaths(node.right, curr + str(node.val) + "->", result)

if __name__ == '__main__':
    sol = Solution()
    t4 = TreeNode(4)
    t3 = TreeNode(3, t4, None)
    t2 = TreeNode(2)
    t1 = TreeNode(1, t2, t3)
    print(sol.binaryTreePaths(t1))

