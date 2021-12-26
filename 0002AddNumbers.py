from typing import Optional
from DataStructures import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        sentinel = ListNode(0)
        curr = sentinel
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            curr.next = ListNode((v1 + v2 + carry) % 10)
            curr = curr.next
            carry = (v1 + v2 + carry) // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return sentinel.next

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

    print(sol.addTwoNumbers(l1,l4))
