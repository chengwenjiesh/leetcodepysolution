class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # keep a double linked list
        # head.next ->    tail
        #. |               |
        # least recent -> most recent
        self.capacity = capacity
        self.head = ListNode()
        self.tail = self.head
        self.kv = {} # k: key v: listnode

    def get(self, key: int) -> int:
        if key in self.kv:
            val = self.kv[key].val
            self.put(key, val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.kv:
            self.tail.next = ListNode(key, value, self.tail)
            self.tail = self.tail.next
            self.kv[key] = self.tail
        else:
            curr = self.kv[key]
            curr.val = value
            
            # if not most recent, adjust list order
            if curr.next:
                # remove listnode from list
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                # place listnode at tail
                self.tail.next = curr
                curr.prev, curr.next = self.tail, None
                self.tail = curr
            
        if len(self.kv) > self.capacity:
            del self.kv[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

if __name__ == '__main__':
    lru = LRUCache(3)
    lru.put(1, '1')
    lru.put(2, '2')
    lru.put(3, '3')
    lru.put(4, '4')
    print(lru.get(1))
    print(lru.get(2))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
