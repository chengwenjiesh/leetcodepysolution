from DataStructures import ListNode

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(), ListNode()
        curr1, curr2 = dummy1, dummy2

        while head:
            nextHead = head.next
            head.next = None
            if head.val < x:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next
            head = nextHead

        curr1.next = dummy2.next
        return dummy1.next


