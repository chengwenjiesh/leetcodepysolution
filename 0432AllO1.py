class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev, self.next = None, None

    def insertAfter(self, newNode):
        oldNext = self.next
        self.next = newNode
        newNode.prev = self
        newNode.next = oldNext
        oldNext.prev = newNode

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # maintain a chain of listnode with increasing word counts
        self.str2Node = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.tail.prev = self.head
        self.head.next = self.tail

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.str2Node:
            currNode = self.head
        else:
            currNode = self.str2Node[key]
            currNode.keys.remove(key)

        if currNode.val + 1 != currNode.next.val:
            newNode = ListNode(currNode.val + 1)
            currNode.insertAfter(newNode)
        else:
            newNode = currNode.next

        newNode.keys.add(key)
        self.str2Node[key] = newNode

        if not currNode.keys and currNode.val != 0:
            currNode.remove()


    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it.
        """
        # key is guaranteed in ds
        currNode = self.str2Node[key]
        currNode.keys.remove(key)
        del self.str2Node[key]

        if currNode.val != 1:
            if currNode.val - 1 != currNode.prev.val:
                newNode = ListNode(currNode.val - 1)
                currNode.prev.insertAfter(newNode)
            else:
                newNode = currNode.prev
            newNode.keys.add(key)
            self.str2Node[key] = newNode

        if not currNode.keys:
            currNode.remove()


    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.tail.prev.val == 0:
            return ""
        for i in self.tail.prev.keys:
            return i

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.head.next.val == 0:
            return ""
        for i in self.head.next.keys:
            return i


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
