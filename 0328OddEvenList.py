from DataStructures import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        oddHead, evenHead = head, head.next
        oddCurr, evenCurr = oddHead, evenHead

        while oddCurr.next and oddCurr.next.next:
            oddCurr.next = oddCurr.next.next
            oddCurr = oddCurr.next
            evenCurr.next = evenCurr.next.next
            evenCurr = evenCurr.next

        oddCurr.next = evenHead
        return oddHead

if __name__ == '__main__':
    sol = Solution()
    l3 = ListNode(3)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    print(sol.oddEvenList(l1))

