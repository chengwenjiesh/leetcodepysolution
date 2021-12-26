from DataStructures import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

if __name__ == '__main__':
    sol = Solution()
    l3 = ListNode(3)
    l2 = ListNode(2)
    l2.next = l3
    l3.next = l2
    l1 = ListNode(1)
    l1.next = l2
    l4 = ListNode(4)
    print(sol.hasCycle(l1))
    print(sol.hasCycle(l4))
