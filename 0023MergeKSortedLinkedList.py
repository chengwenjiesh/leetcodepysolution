from DataStructures import ListNode
import heapq
from typing import List
from typing import Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        min_heap = []
        for idx, node in enumerate(lists):
            if node:
                min_heap.append((node.val, idx, node))
        heapq.heapify(min_heap)

        while min_heap:
            (val, idx, node) = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
            curr.next = node
            curr = curr.next

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
    l9 = ListNode(7)
    l8 = ListNode(6)
    l7 = ListNode(5)
    l7.next = l8
    l8.next = l9

    print(sol.mergeKLists([l1, l4, l7]))

