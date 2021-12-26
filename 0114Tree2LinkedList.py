from DataStructures import TreeNode

class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                suc = curr.left
                while suc.right:
                    suc = suc.right
                suc.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right


if __name__ == '__main__':
    sol = Solution()
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t3 = TreeNode(3, t4, t5)
    t2 = TreeNode(2)
    t1 = TreeNode(1, t2, t3)
    sol.flatten(t1)
    while t1:
        print(t1.val)
        t1 = t1.right

