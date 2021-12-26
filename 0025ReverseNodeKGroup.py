from DataStructures import ListNode

class Solution:
    def reverseKGroup(self, head, k: int):
        if not head:
            return head

        curr = head
        cnt = 1
        while curr and cnt < k:
            curr = curr.next
            cnt += 1

        if not curr or cnt < k:
            return head
        else:
            nextHead = self.reverseKGroup(curr.next, k)
            curr.next = None
            newHead = self.reverseList(head)
            head.next = nextHead
            return newHead


    def reverseList(self, head):
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

if __name__ == '__main__':
    sol = Solution()
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    print(sol.reverseKGroup(l1, 2))

