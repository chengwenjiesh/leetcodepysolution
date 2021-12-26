from DataStructures import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a

if __name__ == '__main__':
    t1 = ListNode(1)
    t2 = ListNode(2, t1)
    t3 = ListNode(3, t1)
    t4 = ListNode(4, t3)
    print(Solution().getIntersectionNode(t2, t4).val)

