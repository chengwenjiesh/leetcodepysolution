from DataStructures import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # circle found
                while head != fast:
                    head = head.next
                    fast = fast.next
                return fast

        return None

if __name__ == '__main__':
    sol = Solution()
    l3 = ListNode(3)
    l2 = ListNode(2)
    l2.next = l3
    l3.next = l2
    l1 = ListNode(1)
    l1.next = l2
    l4 = ListNode(4)
    print(sol.detectCycle(l1).val)
