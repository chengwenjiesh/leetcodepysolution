# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.treeNodes = []
        curr, nxt = [root], []
        while curr:
            for n in curr:
                self.treeNodes.append(n)
                if n.left:
                    nxt.append(n.left)
                if n.right:
                    nxt.append(n.right)
            curr, nxt = nxt, []

    def insert(self, val: int) -> int:
        size = len(self.treeNodes)
        node = TreeNode(val)
        self.treeNodes.append(node)
        parentIdx = (size - 1) // 2
        
        if size % 2 == 0:
            self.treeNodes[parentIdx].right = node
        else:
            self.treeNodes[parentIdx].left = node

        return self.treeNodes[parentIdx].val


    def get_root(self) -> Optional[TreeNode]:
        return self.treeNodes[0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
