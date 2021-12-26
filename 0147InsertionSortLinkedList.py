from DataStructures import ListNode
from typing import Optional

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head

        while curr:
            nextNode = curr.next
            prev, ptr = dummy, dummy.next

            while ptr and ptr != curr and ptr.val < curr.val:
                prev = ptr
                ptr = ptr.next

            prev.next = curr
            curr.next = ptr if curr != ptr else None
            curr = nextNode

        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    l3 = ListNode(9)
    l2 = ListNode(8)
    l1 = ListNode(1)
    l1.next = l2
    l2.next = l3
    l6 = ListNode(4)
    l5 = ListNode(3)
    l4 = ListNode(2)
    l4.next = l5
    l5.next = l6
    l3.next = l4

    print(sol.insertionSortList(l1))
