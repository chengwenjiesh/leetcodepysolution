class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        visited = {head: Node(head.val)}
        dummy = head
        while head:
            if head.next:
                if head.next not in visited:
                    visited[head.next] = Node(head.next.val)
                visited[head].next = visited[head.next]

            if head.random:
                if head.random not in visited:
                    visited[head.random] = Node(head.random.val)
                visited[head].random = visited[head.random]

            head = head.next
            
        return visited[dummy]



