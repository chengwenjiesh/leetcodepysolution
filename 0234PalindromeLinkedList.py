from DataStructures import ListNode
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None
        newHead = self.reverseList(secondHalf)

        while head and newHead:
            if head.val != newHead.val:
                return False
            head = head.next
            newHead = newHead.next

        return True

    def reverseList(self, head):
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

if __name__ == '__main__':
    sol = Solution()
    l3 = ListNode(3)
    l2 = ListNode(2,  l3)
    l1 = ListNode(1, l2)
    print(sol.isPalindrome(l1))
    print(sol.isPalindrome(l3))
