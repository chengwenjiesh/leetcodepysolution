from DataStructures import TreeNode


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        lHead, rHead = self.treeToDoublyList(root.left), self.treeToDoublyList(root.right)
        root.left, root.right = root, root
        return self.connectNode((self.connectNode(lHead, root)), rHead)

    def connectNode(self, node1, node2):
        if not node1 or not node2:
            return node1 or node2

        tail1, tail2 = node1.left, node2.left
        tail1.right = node2
        tail2.right = node1
        node2.left = tail1
        node1.left = tail2

        return node1

if __name__ == '__main__':
    sol = Solution()
    t4 = TreeNode(4)
    t3 = TreeNode(3, None, t4)
    t2 = TreeNode(1)
    t1 = TreeNode(2, t2, t3)
    t = sol.treeToDoublyList(t1)
    curr = t
    while True:
        print(curr.val)
        curr = curr.right
        if curr == t:
            break

