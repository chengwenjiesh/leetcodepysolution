from DataStructures import ListNode
from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        sz = 1
        lastNode = head
        while lastNode.next:
            lastNode = lastNode.next
            sz += 1

        k %= sz
        if not k:
            return head
        lastNode.next = head
        curr = head

        for _ in range(sz - k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None

        return newHead


