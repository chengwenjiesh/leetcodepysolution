from DataStructures import ListNode

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    l3 = ListNode(5)
    l2 = ListNode(3, l3)
    l1 = ListNode(1, l2)
    l6 = ListNode(6)
    l5 = ListNode(4, l6)
    l4 = ListNode(2, l5)
    print(sol.mergeTwoLists(l1, l4))

