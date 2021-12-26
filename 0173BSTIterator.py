from DataStructures import TreeNode

class BSTIterator:

    def __init__(self, root):
        self.toVisit = []
        self._pushAll(root)


    def next(self) -> int:
        if self.hasNext():
            curr = self.toVisit.pop()
            if curr.right:
                self._pushAll(curr.right)
            return curr.val


    def hasNext(self) -> bool:
        return len(self.toVisit) > 0


    def _pushAll(self, node):
        while node:
            self.toVisit.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    t4 = TreeNode(4)
    t3 = TreeNode(3, None, t4)
    t2 = TreeNode(1)
    t1 = TreeNode(2, t2, t3)
    it = BSTIterator(t1)
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
