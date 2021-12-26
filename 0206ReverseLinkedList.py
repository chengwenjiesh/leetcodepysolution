from DataStructures import ListNode
from typing import Optional

class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head

    def reverseList(self, head):
        if not head or not head.next:
            return head

        new_head = None
        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next

        return new_head



if __name__ == '__main__':
    sol = Solution()
    l3 = ListNode(3)
    l2 = ListNode(2)
    l2.next = l3
    l1 = ListNode(1)
    l1.next = l2
    l4 = ListNode(4)
    l3.next = l4
    print(sol.reverseList(l1))
    print(sol.reverseList1(l1))
